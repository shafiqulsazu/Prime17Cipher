<p align="center">
  <img src="HSTU_Logo.png" alt="HSTU Logo" width="250" height="300">
</p>

<h3 align="center">
  Hajee Mohammad Danesh Science and Technology University,Dinajpur-5200.
</h3>
<h3 align="center">
Project Name: Prime17 Cipher Algorithm Design
</h3>

<h3 align="center">
  Course Title: Mathematical Analysis for Computer Science
</h3>

<h3 align="center">
  Course Code: CSE 361
</h3>
<br>
<h1 align="center">Submitted By</h1>

 <p align="center">Md. Shafiqul Islam Sazu<br>Student ID: 2102035<br>Level: 3 Semester: II<br>Department of Computer Science and Engineering</p>
 <br>

<h1 align="center">Submitted To</h1>

 <p align="center">Pankaj Bhowmik<br>Lecturer<br>Department of Computer Science and Engineering</p>


<br><br><br>




## Algorithm Name

**Prime17 Cipher**
The name "Prime17 Cipher" reflects the algorithm’s use of prime numbers for key generation, with "17" (a prime number) emphasizing the mathematical foundation and bitwise shifting operations used in encryption and decryption.

## Algorithm Design

The Prime17 Cipher is a symmetric key cryptographic algorithm that combines prime number-based key generation, modular arithmetic, and bitwise operations (XOR and shifts) to encrypt and decrypt text. The algorithm uses a secret key to control the encryption and decryption processes, ensuring security through mathematical complexity.


Key Components
--------------

**Key:**
A positive integer k (e.g., 17), used to generate a sequence of prime numbers.

**Prime Sequence:**  
For a key k, generate the first n prime numbers, where n is the length of the plaintext.For example, for k=17, use primes like 2, 3, 5, 7, 11, etc.

**Encryption:**
Each character in the plaintext is transformed using:

*   The ASCII value of the character,
    
*   A prime number from the generated sequence,
    
*   Bitwise XOR and left-shift operations,
    
*   Modulo operation using a large prime (e.g., 127).
    

**Decryption:**Reverse the encryption process using the same key and prime sequence to retrieve the original plaintext.

Encryption Algorithm
--------------------

**Input:** Plaintext P, Key k

1.  Generate the first nnn prime numbers, where nnn is the length of PPP.
    
2.  For each character P[i] (where i is the index):
   ```sh
   Convert P[i] to its ASCII value A[i].
   ```
   ```sh
   Compute C[i]=(A[i]⊕Pn[i])mod  127, where Pn[i] is the i-th prime.
   ```
   ```sh     
   Left-shift C[i] by k mod  7 bits (to limit the shift range).
   ```
   ```sh   
   Store C[i] as the ciphertext character.
   ``` 
        
3.  Output the ciphertext C.
    

Decryption Algorithm
--------------------

**Input:** Ciphertext C, Key k

1.  Generate the same sequence of nnn prime numbers using k.
    
2.  For each ciphertext value C[i]:
    
  ```sh
  Right-shift C[i] by k mod 7 bits to undo the left-shift.
  ```
  ```sh   
  Compute A[i]=(C[i]⊕Pn[i])mod  127.
  ```
  ```sh   
  Convert A[i] back to its corresponding ASCII character.
  ``` 
        
3.  Output the plaintext P.
    

Test Case and Experimental Results
----------------------------------

Let’s illustrate the algorithm with an example:

*   **Plaintext:** HELLO MACS
    
*   **Key:** k=17
    
*   **Prime Sequence:** For a 10-character plaintext, use the first 10 primes:2,3,5,7,11,13,17,19,23,29

& Encryption Plaintext:

H (ASCII 72), E (ASCII 69), L (ASCII 76), L (ASCII 76), 0 (ASCII 79), (space, ASCII 32), M (ASCII 77), A (ASCII 65), C (ASCII 67), S (ASCII 83)

Shift value:

Let k =17, so k mod 7=3

This means a left shift by 3 bits, or multiplication by 2<sup>3</sup> = 8

We'll also XOR each character with a unique number in this sequence:

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

For each character:

|ASCII XOR|Value XOR Result|x8 Mod|127 Final Encrypted|
| :- | :- | :- | :- |
|72 2|70|560 560|% 127 = 52 52|
|69 3|70|560 560|% 127 = 52 52|
|76 5|73|584 584|% 127 = 76 76|
|76 7|75|600 600|% 127 = 92 b 7|
|79 11|68|544 544|% 127 = 36 36|
|32 13|45|360 360|% 127 = 106 106|
|77 17|92|736 736|% 127 = 101 101|
|65 19|82|656 656|% 127 = 21 21|
|67 23|84|672 672|% 127 = 37 37|
|8&3 29|78|624|624 % 127 = 117 117|

[52, 52, 76, 92, 36, 106, 101, 21, 37, 117]

### Decryption 

 **Ciphertext**:

[52, 52, 76, 92, 36, 106, 101, 21, 37, 117]

**Parameters**:


| Parameter | Value |
|-----------|-------|
| `k mod 7` | **3** (original shift) |
| Inverse of 8 mod 127 | **111** (because 8 × 111 ≡ 1 mod 127) |

**Per-value process**:

| Cipher | × 111 mod 127 | XOR | After XOR | ASCII | Char |
|-------:|--------------:|----:|----------:|------:|------|
| 52 | 70 | 2 | 72 | 72 | H |
| 52 | 70 | 3 | 69 | 69 | E |
| 76 | 73 | 5 | 76 | 76 | L |
| 92 | 75 | 7 | 76 | 76 | L |
| 36 | 68 | 11 | 79 | 79 | O |
| 106 | 45 | 13 | 32 | 32 | (space) |
| 101 | 92 | 17 | 77 | 77 | M |
| 21 | 82 | 19 | 65 | 65 | A |
| 37 | 84 | 23 | 67 | 67 | C |
| 117 | 78 | 29 | 83 | 83 | S |


**Result**:

## HELLO MACS

##  Pseudocode
```sh
// Encryption
Function Encrypt(Plaintext P, Key k)
    n = length(P)
    Primes = GeneratePrimes(n) // Generate first n primes
    Shift = k mod 7
    Ciphertext C = []
    For i = 0 to n-1
        A = ASCII(P[i])
        Temp = (A XOR Primes[i]) mod 127
        C[i] = (Temp * 2^Shift) mod 127
    EndFor
    Return C

// Decryption
Function Decrypt(Ciphertext C, Key k)
    n = length(C)
    Primes = GeneratePrimes(n)
    Shift = k mod 7
    Plaintext P = []
    For i = 0 to n-1
        Temp = (C[i] / 2^Shift) mod 127 // Floor division
        A = (Temp XOR Primes[i]) mod 127
        P[i] = Character(A)
    EndFor
    Return P

// Helper: Generate first n prime numbers
Function GeneratePrimes(n)
    Primes = []
    num = 2
    While length(Primes) < n
        If isPrime(num)
            Append num to Primes
        num = num + 1
    EndWhile
    Return Primes
```
