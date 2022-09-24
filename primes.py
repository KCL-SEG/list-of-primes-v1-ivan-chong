"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2
    if number_of_primes <= 0:
        return
    while len(list) < number_of_primes:
        if all(num%i != 0 for i in range(2, num)):
            list.append(num)
        num+=1
    return list
