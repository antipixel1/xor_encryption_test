import random
import sys
#Function to generate a random binary key
def generate_random_key(length):
    generator = random.Random()
    key = ""
    for i in range(length):
        key += str((generator.randint(0,1)))
    return key

#Function to XOR encrypt a string with a randomly generated key
def random_xor_encrypt(data):
    data_bytes = bytes(data, 'utf-8')
    data_bits = ""
    for element in data_bytes:
        converted_element = str(bin(element))[2:]
        while (len(converted_element)<8):
            converted_element = "0" + converted_element
        data_bits += converted_element
    key = generate_random_key(len(data_bits))
    encrypted = bin(int(data_bits,2) ^ int(key,2))
    encrypted = str(encrypted)[2:]
    return [encrypted, key]

#Function to convert binary strings to ascii
def bin_to_ascii(data_bin):
    while (len(data_bin)%8 != 0):
        data_bin = "0" + data_bin
    data_ascii = ""
    counter_bits = 0
    converted_byte = ""
    for i in range(len(data_bin)):
        if (counter_bits) == 8:
            data_ascii += chr(int(converted_byte, 2))
            converted_byte = ""
            counter_bits = 0
        converted_byte += data_bin[i]
        counter_bits += 1
    data_ascii += chr(int(converted_byte, 2))
    return data_ascii

#Function to XOR decrypt a string with a specific key
def random_xor_decrypt(data_bits, key):
    decrypted = str(bin(int(data_bits,2) ^ int(key,2)))[2:]
    while (len(decrypted)%8 != 0):
        decrypted = "0" + decrypted
    decrypted_ascii = bin_to_ascii(decrypted)
    return decrypted_ascii

#Driver code
def __main__():
    sys.stdout.reconfigure(encoding='utf-8')
    print("XOR Encryption")
    sample = "When you want foundation repair you want foundation repair, and you like to save a lot of money right? and you like to redacted a lot of redacted right? then you should call HoH SiS. They saved us thousands of dollars on all the redacted that we needed. It was great. I would totally recommend them to anybody. foufoufofofundation When you want the JoJ. They did whatever it took to get the JoJ. We care more about the JoJ than anything else. When it comes to foundation repair in north Texas there is nobody with an A+ rating with a better business bureau, If i had to do it all over again and i had to take redacted all over again, i would still do it all over again. I would do it all over again. I'd do it 15 times over again If i brought 15 houses with foundation problems everytime i would still do it all over again. They do-do the foundation work and we've seen all commercials on TV about the Hercules Hook! and we've seen longer cocks on TV. 100% unsatisfied. hahaHAHAHAHAHAHAHA. UM. We're gonna lift the house wawaonce we get to that point we're gonna lift the house, uh, shim it off and then its its we're gonna do it all over again. And even though there's only a tiny cock they'll redacted you as long as your redacted is standing. 100% guranteed redacted in your redacted. wewawaoncewewoawowow I'm very pleased Kerry worked with me in everyway possible to do it all over again. That aorta do it. Redacted Luigi we gotta do it all over again."
    rand_key = generate_random_key(32)
    encrypted_string = random_xor_encrypt("This is just sample text")
    #encrypted_string = random_xor_encrypt(sample)
    print("Encrypted string in binary:", encrypted_string[0])
    print("Encryption key in binary:", encrypted_string[1])
    data_ascii = bin_to_ascii(encrypted_string[0])
    print("Encrypted string in ascii: ", data_ascii)
    original_string = random_xor_decrypt(encrypted_string[0], encrypted_string[1])
    print("Original string:", original_string)
    
if __name__ == "__main__":
    __main__()