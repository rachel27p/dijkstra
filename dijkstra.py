import sys

INF = 1000000
MAX = 100

def printPath(prev, j):
    if prev[j] == -1:
        return
    printPath(prev, prev[j])
    print(f" -> {j}", end="")

def dijkstra(mulai, akhir, graf, n):
    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    prev = [-1] * (n + 1)

    dist[mulai] = 0

    while True: 
        u = -1
        minDist = INF
        
        for i in range(1, n + 1):
            if not visited[i] and dist[i] < minDist:
                u = i
                minDist = dist[i]
        
        if u == -1 or dist[u] == INF:
            break

        visited[u] = True

        for v in range(1, n + 1):
            if graf[u][v] != 0:
                if dist[v] > dist[u] + graf[u][v]:
                    dist[v] = dist[u] + graf[u][v]
                    prev[v] = u

        
    print(f"Jarak minimal dari node {mulai} ke {akhir}: {dist[akhir]}")
    print(f"Jalur terpendek: {mulai}", end="")
    printPath(prev, akhir)
    print()

    return dist[akhir]

def main():
    print("Algoritma Dijkstra - Mata Kuliah Desain dan Analisis Algoritma")
    n = int(input("\nMasukkan banyak node: "))

    graf = [[0] * (n + 1) for _ in range(n+ 1)]

    print(f"Masukkan matriks ketetanggan ({n} x {n}) dan bobot (0 jika tidak terhubung): ")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            while True:
                try:
                    graf[i][j] = int(input(f"Bobot vertex {i} -> vertex {j}: "))
                    if graf[i][j] >= 0:
                        break
                    else:
                        print("Bobot tidak boleh negatif. Silakan masukkan lagi.")
                except ValueError:
                    print("Masukkan angka yang valid.")
    
    print("\nMatriks Ketetanggan: ")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(graf[i][j], end=" ")
        print()

    while True:
        try:
            mulai = int(input("\nMasukkan node mulai (start): "))
            akhir = int(input("Masukkan node akhir (end): "))

            dijkstra(mulai, akhir, graf, n)

            while True:
                lanjut = input("\nApakah ingin melanjutkan pogram? (y/n): ").lower()
                if lanjut == "y":
                    break
                elif lanjut == "n":
                    print("\nTerima kasih.")
                    sys.exit(0)
                else:
                    print("Inputan salah. Masukkan y atau n.")
        except ValueError:
            print("Masukkan angka yang valid.")
            
if __name__ == "__main__":
    main()