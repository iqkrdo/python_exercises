
def sum_even_nb():
    print("\nSum of even x numbers! Enter numbers. Enter anything else to finish.\n")
    SumEvenNumbers = 0
    try:
        while (1):
            number = int(input("Number: "))
            if number % 2 == 0: SumEvenNumbers += number
    except:
        print(f"The sum is {SumEvenNumbers}")


if __name__ == '__main__':
    sum_even_nb()