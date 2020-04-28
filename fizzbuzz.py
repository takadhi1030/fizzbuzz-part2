def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "Fizz Buzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)

result = fizzbuzz_convert(1)
print(result)
