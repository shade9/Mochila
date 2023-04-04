def knapsack_dynamic(capacity, weights, values, n):
    """
    Implementación del algoritmo de la mochila (knapsack) utilizando enfoque dinámico.
    :param capacity: Capacidad total de la mochila.
    :param weights: Lista de pesos de los elementos.
    :param values: Lista de valores de los elementos.
    :param n: Número total de elementos.
    :return: Valor máximo que se puede obtener en la mochila.
    """

    # Creamos una tabla de tamaño (n+1)x(capacity+1) para almacenar los resultados intermedios.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Llenamos la tabla utilizando un enfoque de programación dinámica.
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                # Si no hay elementos o la capacidad de la mochila es 0, el valor es 0.
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                # Si el peso del elemento actual es menor o igual a la capacidad de la mochila,
                # tomamos el valor máximo entre incluir o excluir el elemento en la mochila.
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # Si el peso del elemento actual es mayor que la capacidad de la mochila,
                # no lo incluimos y tomamos el valor máximo hasta el elemento anterior.
                dp[i][w] = dp[i - 1][w]

    # El resultado se encuentra en la celda dp[n][capacity] de la tabla.
    return dp[n][capacity]


# Ejemplo de uso:

# Datos de entrada: capacidad de la mochila, pesos y valores de los elementos.
capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]
n = len(weights)

# Llamamos a la función knapsack_dynamic y mostramos el resultado.
max_value = knapsack_dynamic(capacity, weights, values, n)
print("Valor máximo en la mochila:", max_value)
