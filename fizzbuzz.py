def fizzbuzz_convert(number):
    if number % 15 == 0:
        print("Fizz Buzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(str(number))

fizzbuzz_convert(1)
fizzbuzz_convert(2)
fizzbuzz_convert(3)
fizzbuzz_convert(4)
fizzbuzz_convert(15)
fizzbuzz_convert(100)

