def process_numbers():
    """
    This function performs various operations on a series of numbers entered by the user.
    It calculates the sum of even numbers, the product of odd numbers, counts prime numbers,
    finds the minimum number with an even digit-reversed number, and finds the maximum
    number after removing odd digits.
    """

    print("Operatii pe numere:")

    # 1. Sum of even numbers
    n = int(input("Dati numarul de numere: "))
    s = 0
    numbers = list(map(int, input().split()))  # Read numbers as a list
    for x in numbers:
        if x % 2 == 0:
            s += x
    print("Suma numerelor pare:", s)

    # 2. Product of odd numbers
    n = int(input("Dati numarul de numere: "))
    p = 1
    numbers = list(map(int, input().split()))
    for x in numbers:
        if x % 2 == 1:
            p *= x
    print("Produsul numerelor impare:", p)

    # 3. Count prime numbers
    n = int(input("Dati numarul de numere: "))
    k = 0
    numbers = list(map(int, input().split()))
    for x in numbers:
        ok = 1
        for d in range(2, x // 2 + 1):
            if x % d == 0:
                ok = 0
                break
        if ok == 1:
            k += 1
    print(k, "numere prime")

    # 4. Minimum number with even digit-reversed number
    n = int(input("Dati numarul de numere: "))
    mn = 10000
    numbers = list(map(int, input().split()))
    for x in numbers:
        inv = 0
        y = x
        while y != 0:
            c = y % 10
            y //= 10
            inv = inv * 10 + c
        if mn > x and inv % 2 == 0:
            mn = x
    print("Minimul numerelor care au inversul cifrelor numar par:", mn)

    # 5. Maximum number after removing odd digits
    n = int(input("Dati numarul de numere: "))
    mx = -10000
    numbers = list(map(int, input().split()))
    for x in numbers:
        y = x
        z = 0
        p = 1
        while y != 0:
            c = y % 10
            y //= 10
            if c % 2 == 0:
                z += c * p
                p *= 10
        if mx < z:
            mx = z
    print("Maximul numerelor din care am eliminat cifrele impare:", mx)


if __name__ == "__main__":
    process_numbers()