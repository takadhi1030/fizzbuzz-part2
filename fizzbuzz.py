def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "Fizz Buzz"

    if number % 5 == 0:
        return "Buzz"

    if number % 3 == 0:
        return "Fizz"

        return str(number)


result = fizzbuzz_convert(1)
print(result)
