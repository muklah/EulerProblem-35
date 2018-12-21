import math

def primeChecking(n, primes):
    if n in primes:
        return primes[n]

    for num in range(2, math.floor(math.sqrt(n)+1)):
        if n % num == 0:
            primes[n] = False
            return False
    primes[n] = True
    return True


def main():
    print("Checking input...")
    count = 0
    primes = {}

    for num in range (2, 1000000):
        q = False
        num = str(num)
        for i in range(len(num)):
            if primeChecking(int(num[i:]+num[:i]), primes):
                q = True
            else:
                q = False
                break
        if q:
            count += 1
    print ("Number of prime numbers:",count)

if __name__ == "__main__":
    main()
