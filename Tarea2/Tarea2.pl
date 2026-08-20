items_principales([espada, pico, carne, pico]).
items_secundarios([hacha, linterna, cuerda]).

% Fase 2 de Recorrido, si la lista esta vacia no hace nada
mostrar_inventario([]).
% pero si la lista esta llena se hace la recursion
mostrar_inventario([H|T]) :- 
    write(H), nl, % Esto ayuda a mostrar el item actual y despues hace un salto de linea
    mostrar_inventario(T). % Esta es la llamada recursiva para poder ir de item en item hasta que la lista este vacia.

procesar_inventario(ItemBuscado, TotalItems, InventarioInvertido, InventarioUnico, InventarioOrdenado) :-
    items_principales(L), % Muestra la lista de items_principales
    items_secundarios(M), % Muestra la lista de items_secundarios
    append(L, M, InventarioTotal), % Une la listas en una sola
    length(InventarioTotal, TotalItems), % Cuenta los items en la lista 
    member(ItemBuscado, InventarioTotal), % Busca un item
    reverse(InventarioTotal, InventarioInvertido), % Cambia el orden de los elementos
    sort(InventarioTotal, InventarioUnico), % Quita los duplicados
    msort(InventarioTotal, InventarioOrdenado), % Se queda con duplicados
    mostrar_inventario(InventarioTotal).