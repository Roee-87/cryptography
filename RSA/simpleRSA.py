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
            msg += chr((pow(c, e, N))) #converts the int back into a char again
    return msg

def main():
    # Start by picking two primes, p and q.  These are kept private!
    p = 13
    q = 29

    #calculate the RSA Modulus N where N = p * q.  This is a public value!   For "small" prime
    #numbers fewer than 100 digits, it's feasible to factor the primes and calculate the private key.
    #Therefore, large values for p and q are required for live systems
    N = p*q

    #calculate the totient phi(N) where phi(N) = (p-1)*(q-1)
    phiN = (p-1)*(q-1)

    #pick a value for e such that 1 < e <= phiN and is coprime to phiN.  This is the PUBLIC KEY
    e = 131

    d = modularInv(e, phiN) #This is the PRIVATE KEY

    print(f"Enter the string to input:  ")
    message = input()

    enc = encrypt(e, N, message)
    dec = decrypt(d, N, enc)

    print(f"Message: {message}")
    print(f"e is the public key: {e}")
    print(f"d is the private key: {d}")
    print(f"N is a public parameter: {N}")
    print(f"enc: {enc}")
    print(f"dec: {dec}")
  

main()



