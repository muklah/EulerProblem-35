import math

# method to checking each number
def primeChecking(n, primes):
    if n in primes:
        return primes[n]

# loop to check numbers if each of it is prime or not
    for num in range(2, math.floor(math.sqrt(n)+1)):
        if n % num == 0:
          # if it's mod of 2 equal 0 then it's not prime and return false for that number in array of rotations number
            primes[n] = False
            return False
   # if it's mod of 2 NOT equal 0 then it's prime and return true for that number in array of rotations number       
    primes[n] = True
    return True


def main():
    print("Checking input...")
    count = 0
    primes = {}

# loop for numbers from 2 to 1000000
    for num in range (2, 1000000):
        boolPrime = False

        # change number from int to string
        num = str(num)

        # loop to get all rotations of each number
        for i in range(len(num)):
            if primeChecking(int(num[i:]+num[:i]), primes):
                boolPrime = True
            else:
                boolPrime = False
                break
        # if all rotations of number are prime then increase counter by one
        if boolPrime:
            count += 1
    print ("Number of prime numbers:",count)

if __name__ == "__main__":
    main()
