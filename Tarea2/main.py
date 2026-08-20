from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from pyswip import Prolog

app = Flask(__name__)
CORS(app)

# Iniciar Prolog y la cargar del archivo
prolog = Prolog()
prolog.consult("Tarea2.pl")

def limpiar_lista(lista_prolog):
    # Esto srive para convertir los datos de prolog para evitar error de Flask
    return [str(elem) for elem in lista_prolog]

# Ruta principal
@app.route('/')
def index():
    return send_file('index.html')

# Endpoint GET para consultar el inventario
@app.route('/inventario', methods=['GET'])
def consultar_inventario():
    item_buscado = request.args.get('item', '').strip().lower()

    if not item_buscado:
        return jsonify({
            'encontrado': False,
            'mensaje': 'Debes ingresar un item a buscar.'
        }), 400

    consulta = f"procesar_inventario({item_buscado}, TotalItems, InventarioInvertido, InventarioUnico, InventarioOrdenado)"

    try:
        resultados = list(prolog.query(consulta))

        if resultados:
            res = resultados[0]
            respuesta = {
                'encontrado': True,
                'item_buscado': item_buscado,
                'total_items': res['TotalItems'],
                'inventario_invertido': limpiar_lista(res['InventarioInvertido']),
                'inventario_unico': limpiar_lista(res['InventarioUnico']),
                'inventario_ordenado': limpiar_lista(res['InventarioOrdenado'])
            }
            return jsonify(respuesta), 200
        else:
            return jsonify({
                'encontrado': False,
                'mensaje': f"El item '{item_buscado}' no se encuentra en el inventario."
            }), 404

    except Exception as e:
        return jsonify({
            'encontrado': False,
            'mensaje': f"Error al procesar la consulta en Prolog: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)