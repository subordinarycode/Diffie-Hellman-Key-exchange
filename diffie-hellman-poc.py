#! /bin/env python3 

# Note this is only a proof of concerpt and is not ment to be used for actual encryption purposes
# The diffie hellman key exchange protocl is ment to be used when keys need to passed over unsecure networks
# The way the protocol works is by sending the prime number and generator over the unsecure network and calculating a public private key pair using the prime number and generator

from Crypto.Util import number
import hashlib

# Both parties need to agree on a high prime number
# You can also use 1024 to be a bit faster when generating
# But it is generally more secure to use 2024 bits and higher
prime_number = number.getPrime(2024)

# Both parties need to agree on a generator
# The generator must less then the prime number
generator = number.getRandomRange(2, prime_number-2)

def generate_keys():
    # Generating a secert key
    # This is private and should never be shared
    secret_key = number.getRandomRange(2, prime_number-2)

    # Doing some math do generate a public key
    # Pretty much the same calc just smaller numbers
    # x = 5^6 % 23
    # x = 5 x 5 x 5 x 5 x 5 x 5 % 23
    public_key = pow(generator, secret_key, prime_number)

    # Return the new public and private keys
    return {
        "public_key": public_key,
        "secret_key": secret_key
    }


def main():
    # Generate a public private key pair for bob
    bob = generate_keys()
    # Generate a public private key pair for charley
    charley = generate_keys()

    # Sanity check making sure the secret keys dont match
    if charley["secret_key"] == bob["secret_key"]:
        print("[-] Something went wrong.\n[-] The bob and charleys secret keys match.")
    else:
        print("[+] Secret keys generated for charley and bob.")

        # Taking bobs public key and combining it with charleys secret key % the prime number
        # Same calc thats in generate_keys()
        charley_shared_secret = pow(bob["public_key"], charley["secret_key"], prime_number)

        # Taking charleys public key and combining it with bobs secret key % the prime number
        # Same calc thats in generate_keys()
        bob_shared_secret = pow(charley["public_key"], bob["secret_key"], prime_number)

        # Converting charleys secret key into bytes
        charley_shared_secret_bytes = charley_shared_secret.to_bytes((charley_shared_secret.bit_length() + 7) // 8, byteorder='big')
        # Converting bobs secret key into bytes
        bob_shared_secret_bytes = bob_shared_secret.to_bytes((bob_shared_secret.bit_length() + 7) // 8, byteorder='big')

        # Creating a session key using the shared secrets
        # A session key is a symmetric encryption key that is generated for each session
        charley_session_key = hashlib.sha256(charley_shared_secret_bytes).hexdigest()
        bob_session_key = x = hashlib.sha256(bob_shared_secret_bytes).hexdigest()

        # Comparing the session keys to make sure they match
        # If they match, the Diffie-Hellman key exchange is complete
        if charley_session_key == bob_session_key:
            print("[+] diffie hellman key exchange complete")
            print(f"[+] Charleys encryption key: {charley_session_key}")
            print(f"[+] Bobs encryption key: {bob_session_key}")




if __name__ == '__main__':
    main()
