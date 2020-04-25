import math


def max_of_two_nums(a, b):
    # Prints max of two numbers
    if a > b:
        print(a)
        return a
    else:
        print(b)
        return b


max_of_two_nums(7, 5)


def fizz_buzz(n):
    # FizzBuzz!
    if n % 3 == 0:
        print("Fizz")
        return "Fizz"
    elif n % 5 == 0:
        print("Buzz")
        return "Buzz"
    elif n % 5 == 0 & n % 3 == 0:
        print("FizzBuzz")
        return "FizzBuzz"
    else:
        return n


fizz_buzz(15)


def check_driver_speed(speed):
    # Function checks driver speed
    # if driver speed is less than 70km its okay,
    # otherwise, add 1 point to registration per 5km above 70
    if speed < 70:
        print("Ok")
    elif speed > 70:
        points = math.floor((speed - 70) / 5)
        print(points)
        if points > 12:
            print("License Suspended")


check_driver_speed(100)


def show_numbers(limit):
    # Function to show numbers between 0 and limit, as well as whether they are even or odd
    numbers = range(0, limit+1, 1)
    for n in numbers:
        if n % 2 == 0:
            print(n, " EVEN")
        else:
            print(n, " ODD")


show_numbers(6)


def sum_of_multiples3(limit):
    # Function to show the sum of multiples of 3 or 5 between 0 and a limit
    numbers = range(0, limit+1, 1)
    number_list = []
    for n in numbers:
        if n % 3 == 0 or n % 5 == 0:
            number_list.append(n)
    summer = sum(number_list)
    print(summer)


sum_of_multiples3(20)


def show_star(rows):
    # Function to print number of stars based on number of rows lol
    stars = range(1, rows+1)
    for n in stars:
        print("*"*stars[n-1])


show_star(5)

def print_prime_nos(limit):



