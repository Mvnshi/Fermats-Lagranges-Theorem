# Munshi Abrar
# Graph Theory
# Group - Grace Hoppper

print("Fermat's theorem on sums of two squares states")
print("an odd prime p can be expressed as p = x^2 + y^2")
print("♥ ♥ ♥ ")
print("Lagrange's theorem on sums of four squares states ")
print("every natural number can be represented as the sum of four integer squares.")
print("♥ ♥ ♥ ")
def sumSquare(n):
    i = 1
    while i * i <= n:
        j = 1
        while j * j <= n:
            if i * i + j * j == n:
                print(f"{i}^2 + {j}^2")
                return True
            j = j + 1
        i = i + 1
    return print("That number doesnt comply with Fermat's theorem make sure its a prime")


def sumFourSquares(a):
    i = 0
    while i * i <= a:
        j = i
        while j * j <= a:
            k = j
            while k * k <= a:
                l = k
                while l * l <= a:

                    if i * i + j * j + k * k + l * l == a:

                        print(f"{i}^2 + {j}^2 + {k}^2 + {l}^2")
                    l = l + 1
                k = k + 1
            j = j + 1
        i = i + 1


if __name__ == "__main__":
    fernant = int(
        input("What number would you like to use Fermat's theorem with? "))
    sumSquare(fernant)
    lagrange = int(
        input("What number would you like to use Lagrange's theorem with? "))

    sumFourSquares(lagrange)
