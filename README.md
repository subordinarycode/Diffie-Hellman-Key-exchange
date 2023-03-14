# Diffie-Hellman Key Exchange Proof of Concept

This is a proof of concept implementation of the Diffie-Hellman key exchange protocol in Python. It is not meant to be used for actual encryption purposes, but rather to demonstrate how the protocol works.

# Usage

To use this implementation, simply run the diffie-hellman.py file in a Python environment. The script will generate two pairs of public and private keys, one for Bob and one for Charley, and will then use these keys to perform the key exchange. If the key exchange is successful, the script will output the shared session key that can be used for encryption.

# Implementation Details

The implementation uses the Crypto.Util.number module to generate large prime numbers and random generators for the protocol. It then generates public and private keys for each party, and combines the public key of one party with the private key of the other party to generate a shared secret key. This shared secret key is then hashed using the SHA-256 algorithm to generate a session key that can be used for encryption.

The implementation is commented throughout to explain the various steps of the protocol and the Python code.

# Steps

The Diffie-Hellman key exchange protocol is a method for two parties to agree on a shared secret key over an insecure communication channel. The protocol works as follows:

Step 1
---
Both parties agree on a large prime number (p) and a random generator (g) that is less than the prime number.

Step 2
---
Both parties generate a random private key (a) and (b), respectively.

Step 3
---
Each party calculates a public key by raising the generator (g) to the power of their private key modulo the prime number p: A = g^a mod p and B = g^b mod p.

Step 4
---
Each party sends their public key to the other party.

Step 5
---
Each party calculates the shared secret key by raising the other party's public key to the power of their own private key modulo the prime number: s = B^a mod p and s = A^b mod p.

Step 6
---
Both parties now have the same shared secret key, which they can use for encryption.

# Security
The security of the protocol relies on the difficulty of computing the private key a or b from the public key A or B, respectively, without knowing the prime number p. This is known as the discrete logarithm problem.

# Applications

The Diffie-Hellman key exchange protocol is widely used in modern cryptography for establishing a shared secret key between two parties.
The protocol is particularly useful in scenarios where the two parties do not have a pre-existing shared secret key, and need to establish one over an insecure communication channel. It is also useful when the two parties want to negotiate a shared key without revealing their private keys to each other.

# Summary
Overall, the Diffie-Hellman key exchange protocol is a powerful tool for secure communication and is an important part of modern cryptography.
