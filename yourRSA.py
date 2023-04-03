import time
import os
import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_random_prime():
    # Get the current time
    current_time = int(time.time())
    
    # Get the number of CPU cores
    num_cores = os.cpu_count()
    
    # Get the amount of RAM in use
    ram_usage = os.popen('free -t -m').readlines()[-1].split()[2]
    
    # Combine the three values into a single seed value
    seed = current_time + num_cores + int(ram_usage)
    
    # Use the seed value to generate a random number
    n = (16807 * seed) % 2147483647
    
    # Check if the number is prime
    while not is_prime(n):
        n = (16807 * n) % 2147483647
    
    return n

def generate_two_random_primes():
    # Generate two random prime numbers
    p = generate_random_prime()
    q = generate_random_prime()
    
    return p, q

def gcd(a, b):
    # Compute the greatest common divisor of a and b using the Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

def findModInverse(a, m):
    # Compute the modular inverse of a modulo m using the extended Euclidean algorithm
    if gcd(a, m) != 1:
        return None # a and m are not relatively prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

# Generate two random prime numbers
p, q = generate_two_random_primes()

# Calculate n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
max_tries = 10000 # Limit the number of attempts to find e
count = 0
e = random.randint(2, phi_n - 1)
while gcd(e, phi_n) != 1:
    e = random.randint(2, phi_n - 1)
    count += 1
    if count >= max_tries:
        print("Could not find a suitable e after", max_tries, "tries.")
        exit()

# Calculate the modular inverse of e modulo phi(n)
d = findModInverse(e, phi_n)

# Public key consists of n and e
public_key = (n, e)

# Private key consists of n and d
private_key = (n, d)

# Print the public and private keys
print("Public key: ", public_key)
print("Private key: ", private_key)