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


Key Components
--------------

- Key: A positive integer k (e.g., 17), used to generate a sequence of prime numbers.

**Prime Sequence:**For a key k, generate the first n prime numbers, where n is the length of the plaintext.For example, for k=17, use primes like 2, 3, 5, 7, 11, etc.

**Encryption:**Each character in the plaintext is transformed using:

*   The ASCII value of the character,
    
*   A prime number from the generated sequence,
    
*   Bitwise XOR and left-shift operations,
    
*   Modulo operation using a large prime (e.g., 127).
    

**Decryption:**Reverse the encryption process using the same key and prime sequence to retrieve the original plaintext.

Encryption Algorithm
--------------------

**Input:** Plaintext P, Key k

1.  Generate the first nnn prime numbers, where nnn is the length of PPP.
    
2.  For each character P\[i\] (where i is the index):
   ```sh
   Convert P\[i\] to its ASCII value A\[i\].
   ```
   ```sh
   Compute C\[i\]=(A\[i\]⊕Pn\[i\])mod  127, where Pn\[i\] is the i-th prime.
   ```
   ```sh     
   Left-shift C\[i\] by k mod  7 bits (to limit the shift range).
   ```
   ```sh   
   Store C\[i\] as the ciphertext character.
   ``` 
        
3.  Output the ciphertext C.
    

Decryption Algorithm
--------------------

**Input:** Ciphertext C, Key k

1.  Generate the same sequence of nnn prime numbers using k.
    
2.  For each ciphertext value C\[i\]:
    
  ```sh
  Right-shift C\[i\] by k mod 7 bits to undo the left-shift.
  ```
  ```sh   
  Compute A\[i\]=(C\[i\]⊕Pn\[i\])mod  127.
  ```
  ```sh   
  Convert A\[i\] back to its corresponding ASCII character.
  ``` 
        
3.  Output the plaintext P.
    

Test Case and Experimental Results
----------------------------------

Let’s illustrate the algorithm with an example:

*   **Plaintext:** HELLO MACS
    
*   **Key:** k=17
    
*   **Prime Sequence:** For a 10-character plaintext, use the first 10 primes:2,3,5,7,11,13,17,19,23,29
