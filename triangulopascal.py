class TrianguloTartaglia:
    def __init__(self, n):
        self.n = n
        self.triangulo = self.calcular_triangulo()

    def calcular_triangulo(self):
        triangulo = [[1]]

        for i in range(1, self.n):
            fila_anterior = triangulo[i-1]
            nueva_fila = [1]

            for j in range(1, i):
                nuevo_elemento = fila_anterior[j-1] + fila_anterior[j]
                nueva_fila.append(nuevo_elemento)

            nueva_fila.append(1)
            triangulo.append(nueva_fila)

        return triangulo

    def imprimir_triangulo(self):
        for fila in self.triangulo:
            print(fila)

# Ejemplo de uso
n = 50


triangulo = TrianguloTartaglia(n)
triangulo.imprimir_triangulo()
