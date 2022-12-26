def egcd(a, b):
    s = p; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r !=0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

def modularInv(a, b):
    gcd, x, y = egcd(a, b)

    if x < 0:
        x += m
        return x

def encrypt(e, n, msg):
    cipher = ""

    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, n)) + " "

    return cipher

def decrypt(d, n, cipher):
    msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, n))

    return msg

def main():
    print("Hello, RSA!")

    p = 11
    q = 13
    n = p*q
    phin = (p - 1) * (q - 1)

    e = 13
    d = modularInv(e, phin)

    msg = "Hello, RSA!"

    enc = encrypt(e, n, msg)
    dec = decrypt(d, n, enc)

    print(f"Message: {msg}")
    print(f"e: {e}")
    print(f"d: {d}")
    print(f"n: {n}")
    print(f"enc: {enc}")
    print(f"dec: {dec}")

main()
