def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def encrypt(plaintext, key):
    n = len(plaintext)
    primes = generate_primes(n)
    shift = key % 7
    ciphertext = []
    for i in range(n):
        ascii_val = ord(plaintext[i])
        temp = (ascii_val ^ primes[i]) % 127
        cipher_val = (temp << shift) % 127
        ciphertext.append(chr(cipher_val))
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    n = len(ciphertext)
    primes = generate_primes(n)
    shift = key % 7
    plaintext = []
    for i in range(n):
        cipher_val = ord(ciphertext[i])
        temp = (cipher_val >> shift) % 127
        ascii_val = (temp ^ primes[i]) % 127
        plaintext.append(chr(ascii_val))
    return ''.join(plaintext)

# Test case
plaintext = "HELLO MACS"
key = 17
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted_text}")
