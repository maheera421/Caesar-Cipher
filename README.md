# Caesar-Cipher


# 🎮 Game Description - Caesar Cipher:

The Caesar Cipher is a simple and classic encryption technique. In this game, you can either encode a message (encrypt it) or decode an already encoded message (decrypt it). The cipher involves shifting each letter in the plaintext by a fixed number of positions down or up the alphabet, resulting in a secret message. It's a fun and educational way to explore the world of cryptography!


# 🚀 How the Code Works:

1. The user is asked to choose between encoding or decoding a message by typing 'encode' or 'decode'.

2. The user inputs the message they want to process. The message is converted to lowercase to ensure consistency.

3. The user specifies the shift value, which is the number of positions each letter should be shifted in the alphabet. If the shift value is greater than 26, it is reduced modulo 26 to stay within the bounds of the alphabet.

4. Depending on whether the user chose to encode or decode, the shift value is applied either positively (for encoding) or negatively (for decoding).

5. The code then processes each character in the input message:
   - If the character is not in the alphabet (e.g., numbers, symbols, spaces), it is included in the result as is.
   - If the character is in the alphabet, its position in the alphabet is determined, and the shift is applied to calculate the new position. The character corresponding to the new position in the alphabet is added to the result.

6. The resulting message (encoded or decoded) is displayed to the user.

7. After processing one message, the user is given the option to restart the program to encode or decode another message.


# 🔐 Code Specifications:

• The code uses external modules `art` and `sheet`, respectively. These files are not provided and are mentioned as private. Users must request access to them separately.

• The user can choose to encode or decode messages using a Caesar Cipher with a specified shift value.

• The code ensures that the shift value stays within the bounds of the alphabet (0 to 25).

• The code works with lowercase text and maintains the original case for non-alphabet characters.
 
• It offers the option to restart the program to process multiple messages.


# 📝 Note:

Please note that the `art` and `sheet` files used in this code are kept private and are not included in the code posted on GitHub. Users who wish to run this code will need to request access to these files separately.
