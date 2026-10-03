from ceasar import encrypt, decrypt

print("===== CEASAR CIPHER =====")
plaintext = input("Enter message: ")
shift = int(input("Enter shift key: "))


#plaintext to ciphertext
ciphertext = encrypt(plaintext, shift)

#ciphertext to back to plaintext
decrypted = decrypt(ciphertext, shift)

print("Plaintext :", plaintext)
print("Shift key :", shift)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)