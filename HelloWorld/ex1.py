
def sum_even_nb():
    print("\nSum of even x numbers! Enter numbers. Enter anything else to finish.\n")
    SumEvenNumbers = 0
    ProductOddNumbers = 1
    try:
        while (1):
            number = int(input("Number: "))
            if number % 2 == 0: SumEvenNumbers += number
            else: ProductOddNumbers *= number
    except:
        print(f"The sum of even numbers is {SumEvenNumbers}")
        print(f"The product of odd numbers is {SumEvenNumbers}")


if __name__ == '__main__':
    sum_even_nb()