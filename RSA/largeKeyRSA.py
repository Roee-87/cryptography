import random

def rabinMiller(n, d):
    a = random.randint(2, (n - 2) - 2)
    x = pow(a, int(d), n) # a^d%n
    if x == 1 or x == n - 1:
        return True

    # square x
    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2

        if x == 1:
            return False
        elif x == n - 1:
            return True
    
    # is not prime
    return False

def isPrime(n):
    if n < 2:
        return False
    
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if n in lowPrimes:
        return True 
    
    #if low primes divide into n
    for prime in lowPrimes:
        if n % prime ==0:
            return False
        # find number c such that c * 2 ^ r = n - 1
    c = n - 1 # c even bc n not divisible by 2
    while c % 2 == 0:
        c /= 2 # make c odd

    # prove not prime 128 times
    for i in range(128):
        if not rabinMiller(n, c):
            return False

    return True
    
     


def generateKeys(keysize=1024):
    e = d = N = 0.0
    # get prime numbers p and q
    p = generateLargePrime(keysize)
    q = generateLargePrime(keysize)

    N = p * q

    phiN = (p-1) * (q-1)

    # choose e (PUBLIC KEY)
    # e must be coprime with phiN and 1 < 3 <= phiN

    while True:
        e = random.randrange(2**(keysize-1), 2**(keysize)-1)
        if (isCoPrime(e,phiN)):
            break
    d = modularInv(e, phiN)
    
    #calculate d (PRIVATE KEY)
    #d is the modular inverse of e with respect to phiN
    # e * d (mod(phiN)) == 1




def generateLargePrime(keysize):
    """
    return random Large prime number 
    """

    while True:
        num = random.randrange(2**(keysize - 1), 2**(keysize)-1)
        if (isPrime(num)):
            return num

def isCoPrime(p, q):
    """
    returns true if gcd(p,q) == 1 
    """
    return gcd(p, q) == 1

def gcd(p, q):
    '''
    uses the Euclidean algorthm to find greatest common denominator of p and q
    '''
    while q:
        p, q = q, p%q
    return p


def modularInv(a,b):
    return pow(a,-1,b)

def encrypt(d, N, msg):
    cipher = ""

    for c in msg:
        m = ord(c) #converts a char to a numerical value
        cipher += str(pow(m, d, N)) + " " #the + " " adds a space between values so we can use .split() later in the encode function

    return cipher

def decrypt(e, N, cipher):
    msg = ""
    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr((pow(c, e, N)))
    return msg

def main():

    enc = encrypt(e, N, message)
    dec = decrypt(d, N, enc)

    print(f"Message: {message}")
    print(f"e: {e}")
    print(f"d is the private key: {d}")
    print(f"N: {N}")
    print(f"enc: {enc}")
    print(f"dec: {dec}")
  

main()



