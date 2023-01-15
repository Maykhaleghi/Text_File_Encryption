class data():
'''the parent class'''
    
    def __init__ (self, text):
        self.text = text

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def to_hex (self):

        #this method converts simple text to hexdecimal form.
        hex_list = []
        for char in self.text:
            string = char.encode('utf-8')
            hex_str = string.hex()
            hex_list.append("0x" + hex_str)

        if len(hex_list) < 16:
            n = 16 - len(hex_list)
            for i in range(0, n):
                hex_list.append("0x00")
        return hex_list

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def add_key (self, key):

        #this method takes a *simple* text in format of str.
        text = ""
        hex_str = self.to_hex()
        hex_key = key.to_hex()
        
        for i,j in zip(hex_str, hex_key):
            hexed = hex(int(i, 16) ^ int(j, 16))
            if len(hexed) == 3:
                t = "0" + hexed[2:]
                text += t
            else:
                text += hexed[2:]

        return data(text)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def add_key0 (self, key):

        #this method takes hexadecimal *string* in form of str.
        #each element of this string has 0x in the beginning.
        text = ""
        hex_str = self.text
        hex_key = key.to_hex()
        new_hex_str = []
        
        for i in range(0, len(hex_str), 2):
            summ = "0x" + hex_str[i] + hex_str[i+1]
            new_hex_str.append(summ)
            
        for i,j in zip(new_hex_str, hex_key):
            hexed = hex(int(i, 16) ^ int(j, 16))
            if len(hexed) == 3:
                t = "0" + hexed[2:]
                text += t
            else:
                text += hexed[2:]
                
        return data(text)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def add_key_hex (self, key):

        #this method takes hexadecimal *list* in form of str.
        #each element of this string has 0x in the beginning.
        text = ""
        hex_list = self.text
        hex_key = key.to_hex()
        new_hex_list = []
        
        for i in range(0, len(hex_list)):
            hexed = hex(hex_list[i])
            new_hex_list.append(hexed)
            
        for i,j in zip(new_hex_list, hex_key):
            hexed = hex(int(i, 16) ^ int(j, 16))
            if len(hexed) == 3:
                t = "0" + hexed[2:]
                text += t
            else:
                text += hexed[2:]
                
        return data(text)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def s_box (self):

        s_box = [
        [int('63', 16), int('7c', 16), int('77', 16), int('7b', 16), int('f2', 16), int('6b', 16), int('6f', 16), int('c5', 16), int(
        '30', 16), int('01', 16), int('67', 16), int('2b', 16), int('fe', 16), int('d7', 16), int('ab', 16), int('76', 16)],
        [int('ca', 16), int('82', 16), int('c9', 16), int('7d', 16), int('fa', 16), int('59', 16), int('47', 16), int('f0', 16), int(
        'ad', 16), int('d4', 16), int('a2', 16), int('af', 16), int('9c', 16), int('a4', 16), int('72', 16), int('c0', 16)],
        [int('b7', 16), int('fd', 16), int('93', 16), int('26', 16), int('36', 16), int('3f', 16), int('f7', 16), int('cc', 16), int(
        '34', 16), int('a5', 16), int('e5', 16), int('f1', 16), int('71', 16), int('d8', 16), int('31', 16), int('15', 16)],
        [int('04', 16), int('c7', 16), int('23', 16), int('c3', 16), int('18', 16), int('96', 16), int('05', 16), int('9a', 16), int(
        '07', 16), int('12', 16), int('80', 16), int('e2', 16), int('eb', 16), int('27', 16), int('b2', 16), int('75', 16)],
        [int('09', 16), int('83', 16), int('2c', 16), int('1a', 16), int('1b', 16), int('6e', 16), int('5a', 16), int('a0', 16), int(
        '52', 16), int('3b', 16), int('d6', 16), int('b3', 16), int('29', 16), int('e3', 16), int('2f', 16), int('84', 16)],
        [int('53', 16), int('d1', 16), int('00', 16), int('ed', 16), int('20', 16), int('fc', 16), int('b1', 16), int('5b', 16), int(
        '6a', 16), int('cb', 16), int('be', 16), int('39', 16), int('4a', 16), int('4c', 16), int('58', 16), int('cf', 16)],
        [int('d0', 16), int('ef', 16), int('aa', 16), int('fb', 16), int('43', 16), int('4d', 16), int('33', 16), int('85', 16), int(
        '45', 16), int('f9', 16), int('02', 16), int('7f', 16), int('50', 16), int('3c', 16), int('9f', 16), int('a8', 16)],
        [int('51', 16), int('a3', 16), int('40', 16), int('8f', 16), int('92', 16), int('9d', 16), int('38', 16), int('f5', 16), int(
        'bc', 16), int('b6', 16), int('da', 16), int('21', 16), int('10', 16), int('ff', 16), int('f3', 16), int('d2', 16)],
        [int('cd', 16), int('0c', 16), int('13', 16), int('ec', 16), int('5f', 16), int('97', 16), int('44', 16), int('17', 16), int(
        'c4', 16), int('a7', 16), int('7e', 16), int('3d', 16), int('64', 16), int('5d', 16), int('19', 16), int('73', 16)],
        [int('60', 16), int('81', 16), int('4f', 16), int('dc', 16), int('22', 16), int('2a', 16), int('90', 16), int('88', 16), int(
        '46', 16), int('ee', 16), int('b8', 16), int('14', 16), int('de', 16), int('5e', 16), int('0b', 16), int('db', 16)],
        [int('e0', 16), int('32', 16), int('3a', 16), int('0a', 16), int('49', 16), int('06', 16), int('24', 16), int('5c', 16), int(
        'c2', 16), int('d3', 16), int('ac', 16), int('62', 16), int('91', 16), int('95', 16), int('e4', 16), int('79', 16)],
        [int('e7', 16), int('c8', 16), int('37', 16), int('6d', 16), int('8d', 16), int('d5', 16), int('4e', 16), int('a9', 16), int(
        '6c', 16), int('56', 16), int('f4', 16), int('ea', 16), int('65', 16), int('7a', 16), int('ae', 16), int('08', 16)],
        [int('ba', 16), int('78', 16), int('25', 16), int('2e', 16), int('1c', 16), int('a6', 16), int('b4', 16), int('c6', 16), int(
        'e8', 16), int('dd', 16), int('74', 16), int('1f', 16), int('4b', 16), int('bd', 16), int('8b', 16), int('8a', 16)],
        [int('70', 16), int('3e', 16), int('b5', 16), int('66', 16), int('48', 16), int('03', 16), int('f6', 16), int('0e', 16), int(
        '61', 16), int('35', 16), int('57', 16), int('b9', 16), int('86', 16), int('c1', 16), int('1d', 16), int('9e', 16)],
        [int('e1', 16), int('f8', 16), int('98', 16), int('11', 16), int('69', 16), int('d9', 16), int('8e', 16), int('94', 16), int(
        '9b', 16), int('1e', 16), int('87', 16), int('e9', 16), int('ce', 16), int('55', 16), int('28', 16), int('df', 16)],
        [int('8c', 16), int('a1', 16), int('89', 16), int('0d', 16), int('bf', 16), int('e6', 16), int('42', 16), int('68', 16), int(
        '41', 16), int('99', 16), int('2d', 16), int('0f', 16), int('b0', 16), int('54', 16), int('bb', 16), int('16', 16)]]
        
        mylist = list(self.text)
        slist = []

        #we iterate through the list.
        #we need pairs.
        #the first element of each pairs tells us the number of the row.
        #and the second element tells us the number of column.
        for i in range (0,32,2):
            r = int(mylist[i], 16)
            c = int(mylist[i+1], 16)
            slist.append(s_box[r][c]) 
            
        return data(slist)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def inverse_s_box (self):
        
        inverse_s_box = [
        [int('52', 16), int('09', 16), int('6a', 16), int('d5', 16), int('30', 16), int('36', 16), int('a5', 16), int('38', 16), int(
        'bf', 16), int('40', 16), int('a3', 16), int('9e', 16), int('81', 16), int('f3', 16), int('d7', 16), int('fb', 16)],
        [int('7c', 16), int('e3', 16), int('39', 16), int('82', 16), int('9b', 16), int('2f', 16), int('ff', 16), int('87', 16), int(
        '34', 16), int('8e', 16), int('43', 16), int('44', 16), int('c4', 16), int('de', 16), int('e9', 16), int('cb', 16)],
        [int('54', 16), int('7b', 16), int('94', 16), int('32', 16), int('a6', 16), int('c2', 16), int('23', 16), int('3d', 16), int(
        'ee', 16), int('4c', 16), int('95', 16), int('0b', 16), int('42', 16), int('fa', 16), int('c3', 16), int('4e', 16)],
        [int('08', 16), int('2e', 16), int('a1', 16), int('66', 16), int('28', 16), int('d9', 16), int('24', 16), int('b2', 16), int(
        '76', 16), int('5b', 16), int('a2', 16), int('49', 16), int('6d', 16), int('8b', 16), int('d1', 16), int('25', 16)],
        [int('72', 16), int('f8', 16), int('f6', 16), int('64', 16), int('86', 16), int('68', 16), int('98', 16), int('16', 16), int(
        'd4', 16), int('a4', 16), int('5c', 16), int('cc', 16), int('5d', 16), int('65', 16), int('b6', 16), int('92', 16)],
        [int('6c', 16), int('70', 16), int('48', 16), int('50', 16), int('fd', 16), int('ed', 16), int('b9', 16), int('da', 16), int(
        '5e', 16), int('15', 16), int('46', 16), int('57', 16), int('a7', 16), int('8d', 16), int('9d', 16), int('84', 16)],
        [int('90', 16), int('d8', 16), int('ab', 16), int('00', 16), int('8c', 16), int('bc', 16), int('d3', 16), int('0a', 16), int(
        'f7', 16), int('e4', 16), int('58', 16), int('05', 16), int('b8', 16), int('b3', 16), int('45', 16), int('06', 16)],
        [int('d0', 16), int('2c', 16), int('1e', 16), int('8f', 16), int('ca', 16), int('3f', 16), int('0f', 16), int('02', 16), int(
        'c1', 16), int('af', 16), int('bd', 16), int('03', 16), int('01', 16), int('13', 16), int('8a', 16), int('6b', 16)],
        [int('3a', 16), int('91', 16), int('11', 16), int('41', 16), int('4f', 16), int('67', 16), int('dc', 16), int('ea', 16), int(
        '97', 16), int('f2', 16), int('cf', 16), int('ce', 16), int('f0', 16), int('b4', 16), int('e6', 16), int('73', 16)],
        [int('96', 16), int('ac', 16), int('74', 16), int('22', 16), int('e7', 16), int('ad', 16), int('35', 16), int('85', 16), int(
        'e2', 16), int('f9', 16), int('37', 16), int('e8', 16), int('1c', 16), int('75', 16), int('df', 16), int('6e', 16)],
        [int('47', 16), int('f1', 16), int('1a', 16), int('71', 16), int('1d', 16), int('29', 16), int('c5', 16), int('89', 16), int(
        '6f', 16), int('b7', 16), int('62', 16), int('0e', 16), int('aa', 16), int('18', 16), int('be', 16), int('1b', 16)],
        [int('fc', 16), int('56', 16), int('3e', 16), int('4b', 16), int('c6', 16), int('d2', 16), int('79', 16), int('20', 16), int(
        '9a', 16), int('db', 16), int('c0', 16), int('fe', 16), int('78', 16), int('cd', 16), int('5a', 16), int('f4', 16)],
        [int('1f', 16), int('dd', 16), int('a8', 16), int('33', 16), int('88', 16), int('07', 16), int('c7', 16), int('31', 16), int(
        'b1', 16), int('12', 16), int('10', 16), int('59', 16), int('27', 16), int('80', 16), int('ec', 16), int('5f', 16)],
        [int('60', 16), int('51', 16), int('7f', 16), int('a9', 16), int('19', 16), int('b5', 16), int('4a', 16), int('0d', 16), int(
        '2d', 16), int('e5', 16), int('7a', 16), int('9f', 16), int('93', 16), int('c9', 16), int('9c', 16), int('ef', 16)],
        [int('a0', 16), int('e0', 16), int('3b', 16), int('4d', 16), int('ae', 16), int('2a', 16), int('f5', 16), int('b0', 16), int(
        'c8', 16), int('eb', 16), int('bb', 16), int('3c', 16), int('83', 16), int('53', 16), int('99', 16), int('61', 16)],
        [int('17', 16), int('2b', 16), int('04', 16), int('7e', 16), int('ba', 16), int('77', 16), int('d6', 16), int('26', 16), int(
        'e1', 16), int('69', 16), int('14', 16), int('63', 16), int('55', 16), int('21', 16), int('0c', 16), int('7d', 16)]]

        mylist = list(self.text)
        slist = []

        #we iterate through the list.
        #we need pairs.
        #the first element of each pairs tells us the number of the row.
        #and the second element tells us the number of column.
        for i in range (0,32,2):
            r = int(mylist[i], 16)
            c = int(mylist[i+1], 16)
            slist.append(inverse_s_box[r][c])
            
        return data(slist)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def permutation (self):
        mylist =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        slist = self.text

        mylist[0], mylist[1], mylist[2], mylist[3] =  slist[2], slist[8], slist[12], slist[5]
        mylist[4], mylist[5], mylist[6], mylist[7] =  slist[9], slist[0], slist[14], slist[4]
        mylist[8], mylist[9], mylist[10], mylist[11] =  slist[11], slist[1], slist[15], slist[6]
        mylist[12], mylist[13], mylist[14], mylist[15] =  slist[3], slist[10], slist[7], slist[13]
        finallist = []
        
        for i in range (0,16):
            m = hex(mylist[i])
            if len(m) == 3:
                n = "0" + m[2:]
                finallist.append(n)
            else:  
                finallist.append(m[2:])
        f = "".join(finallist)
        
        return data(f)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def permutation_reverse (self):
        
        mylist =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        hex_text = list(self.text)
        clist = []

        #because the string is 32 charachters long,
        #we need these characters as pairs
        #each pair resembels a character in our text.
        for i in range (0, 32, 2):
            t = hex_text[i] + hex_text[i+1]
            clist.append(t)

        #now that we have pairs we do the permutation.
        mylist[0], mylist[1], mylist[2], mylist[3] =  clist[5], clist[9], clist[0], clist[12]
        mylist[4], mylist[5], mylist[6], mylist[7] =  clist[7], clist[3], clist[11], clist[14]
        mylist[8], mylist[9], mylist[10], mylist[11] =  clist[1], clist[4], clist[13], clist[8]
        mylist[12], mylist[13], mylist[14], mylist[15] =  clist[2], clist[15], clist[6], clist[10]
        finallist = []

        #to turn the list to string.
        f = "".join(mylist)
        
        return data(f)

    
#########################################################################    

class block_cipher(data):
'''the child class'''
    
    def __init__ (self, text):
        super().__init__(text)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def encryption (self, key):
        
        def rounds(string, key):
            R1 = string.add_key0(key)
            R2 = R1.s_box()
            R3 = R2.permutation()
            return R3

        R1 = self.add_key(key)
        R2 = R1.s_box()
        R3 = R2.permutation()
        for i in range (0, 9):
            R3 = rounds(R3, key)
            
        return R3

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def decryption (self, key):

        def rounds(string, key):
            R1 = string.permutation_reverse()
            R2 = R1.inverse_s_box()
            R3 = R2.add_key_hex(key)
            return R3

        R1 = self.permutation_reverse()
        R2 = R1.inverse_s_box()
        R3 = R2.add_key_hex(key)
        for i in range (0, 9):
            R3 = rounds(R3, key)
            
        return R3


#########################################################################

with open("text.txt", "r") as mytext:
    maintext = mytext.read()
    print("~~~THE PLAIN TEXT FILE THAT WE JUST OPENED:")
    print(maintext)
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("the number of characters in the *plaintext* file is:" ,len(maintext))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    key = data("Thats my Kung Fu")
    
    #to break the text to 128_bit blocks.
    #each block contains 16 characters.
    n = len(maintext)//16
    m = n * 16
    final_cipher = ""
    for j in range (0, m, 16):
        plainstr = block_cipher(maintext[j:j+16])
        #print(plainstr.text)
        ciphertext = plainstr.encryption(key)
        final_cipher += ciphertext.text
    plainstrr = block_cipher(maintext[m:])
    #print(plainstrr.text)
    chiphertext = plainstrr.encryption(key)
    final_cipher += ciphertext.text

    print("~~~THE RESULT OF OUR ENCRYPTION:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(final_cipher)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("#############################################################################\n")

    #to write the encrypted text in a file.
    with open("ciphertext.txt", "w") as text:
        maintext = text.write(final_cipher)


#############################################################################

with open("ciphertext.txt", "r") as mytext:
    maintext = mytext.read()
    print("~~~THE CIPHER TEXT FILE THAT WE JUST OPENED:")
    print(maintext)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("the number of characters in the *encrypted* file is:" ,len(maintext))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    key = data("Thats my Kung Fu")

    #to break the text to 128_bit blocks.
    #each block contains 32 characters.
    original_hex = ""
    for j in range (0, len(maintext), 32):
        plainstr = block_cipher(maintext[j:j+32])
        ciphertext = plainstr.decryption(key)
        original_hex += ciphertext.text   

    print("~~~THE RESULT OF OUR DECRYPTION:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(original_hex)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #to convert the hexdecimal to text.
    bytes_object = bytes.fromhex(original_hex)
    org_string = bytes_object.decode("utf-8")
    print("~~~OUR DECRYPTED TEXT:")
    print(org_string)

    #to write the decrypted text in a file.
    with open("cipher_text.txt", "w") as text:
        maintext = text.write(org_string)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

