from cs import key

def decryption():
    user_message=input("Please enter plaintext up to 16 hex characters:").strip()
    user_key=input("Enter key in plain text: ").strip()

    message_hex=""
    pos=0
    while pos < len(user_message) and pos < 8:
        char=user_message[pos]
        code=ord(char)

        if code<16:
            message_hex= message_hex+"0"+ format(code,'X')
        else:
            message_hex=message_hex+ format(code,'X')
        pos+=1

    while len(message_hex)<16:
        message_hex=message_hex+"00"

    if len(message_hex)>16:
        message_hex=message_hex[:16]


    key_hex=""
    pos2=0
    while pos2<len(user_key):
        char2=user_key[pos2]
        code2=ord(char2)

        if code2<16:
            key_hex= key_hex+"0"+ format(code,'X')
        else:
            key_hex=key_hex+ format(code,'X')
        pos+=1

    while len(key_hex)<16:
        key_hex=key_hex+"00"

    if len(key_hex)>16:
        key_hex=key_hex[:16]
    
    try:
        message_value=int(message_hex,16)
        key_value=int(key_hex,16)
    except:
        print("Conversion error")
        return None
    
    message_bits=format(message_value,'064b')
    key_bits=format(key_value,'064b')


    PC1 = [
57,49,41,33,25,17,9,
1,58,50,42,34,26,18,
10,2,59,51,43,35,27,
19,11,3,60,52,44,36,
63,55,47,39,31,23,15,
7,62,54,46,38,30,22,
14,6,61,53,45,37,29,
21,13,5,28,20,12,4
]
    

    PC2 = [
14,17,11,24,1,5,
3,28,15,6,21,10,
23,19,12,4,26,8,
16,7,27,20,13,2,
41,52,31,37,47,55,
30,40,51,45,33,48,
44,49,39,56,34,53,
46,42,50,36,29,32
]

    F_permutation = [
40,8,48,16,56,24,64,32,
39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,
37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,
35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,
33,1,41,9,49,17,57,25
]

    IP = [
58,50,42,34,26,18,10,2,
60,52,44,36,28,20,12,4,
62,54,46,38,30,22,14,6,
64,56,48,40,32,24,16,8,
57,49,41,33,25,17,9,1,
59,51,43,35,27,19,11,3,
61,53,45,37,29,21,13,5,
63,55,47,39,31,23,15,7
]


    IP_INV = [
40,8,48,16,56,24,64,32,
39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,
37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,
35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,
33,1,41,9,49,17,57,25
]

    E_table = [
32,1,2,3,4,5,
4,5,6,7,8,9,
8,9,10,11,12,13,
12,13,14,15,16,17,
16,17,18,19,20,21,
20,21,22,23,24,25,
24,25,26,27,28,29,
28,29,30,31,32,1
]

    P_table = [
16,7,20,21,29,12,28,17,
1,15,23,26,5,18,31,10,
2,8,24,14,32,27,3,9,
19,13,30,6,22,11,4,25
]


    S_BOXES = [
# S1
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
# S2
[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],
# S3
[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
],
# S4
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],
# S5
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
# S6
[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
],
# S7
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
# S8
[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]
]
    #Here I made it into 56 bits and divided into left and right half

    key56 = ""
    idx = 0
    while idx < 56:
        pos = PC1[idx]
        key56 = key56 + key_bits[pos - 1]
        idx = idx + 1

    left_key = key56[0:28]
    right_key = key56[28:56]

    #Then I started the shifting

    round_key_list = []
    round_number = 1
    while round_number <= 16:
        if round_number == 1 or round_number == 2 or round_number == 9 or round_number == 16:
            shifts_needed = 1
        else:
            shifts_needed = 2

        shift_count = 0
        while shift_count < shifts_needed:
        # shift left_key
            first_bit_left = left_key[0]

        new_left = ""
        left_index = 1
        while left_index < len(left_key):
            new_left = new_left + left_key[left_index]
            left_index = left_index + 1
            left_key = new_left + first_bit_left

        # shift right_key
        first_bit_right = right_key[0]
        new_right = ""
        right_index = 1
        while right_index < len(right_key):
            new_right = new_right + right_key[right_index]
            right_index = right_index + 1
            right_key = new_right + first_bit_right

            shift_count+= 1
        

        combined_key = left_key + right_key
        subkey = ""
        pc2_index = 0
        while pc2_index < 48:
            pick_pos = PC2[pc2_index]
            subkey = subkey + combined_key[pick_pos - 1]
            pc2_index = pc2_index + 1

        round_key_list.append(subkey)
        round_number+= 1

    # Here I started Initial permutation on message
    permuted = ""
    perm_index = 0
    while perm_index < 64:
        take_pos = IP[perm_index]
        permuted = permuted + message_bits[take_pos - 1]
        perm_index = perm_index + 1

    left = permuted[0:32]#L0
    right = permuted[32:64]#R0

    #Here I made the 16 Feistel rounds using the 16 subkeys in order
    r = 0
    while r < 16:
    # expansion to the right side to be 48 bits
        expanded_right = ""
        expand_index = 0
        while expand_index < 48:
            take_e = E_table[expand_index]
            expanded_right = expanded_right + right[take_e - 1]
            expand_index += 1

    # xored the right side with round keys
        rk = round_key_list[r]
        xored = ""
        xored_index = 0
        while xored_index < 48:
            if expanded_right[xored_index] == rk[xored_index]:
                xored = xored + "0"
            else:
                xored = xored + "1"
            xored_index = xored_index + 1

        # Applied S-boxes to turn them from groups of 6 bits to 4 bits
        sbox_result = ""
        sb_num = 0
        while sb_num < 8:
            #This here is basically the calculation made from the rows and coloumns
            start = sb_num * 6
            block6 = xored[start:start+6]
            row_bits = block6[0] + block6[5]
            col_bits = block6[1:5]
            row_val = int(row_bits, 2)
            col_val = int(col_bits, 2)
            sbox_index_find = row_val * 16 + col_val
            box = S_BOXES[sb_num]
            val = box[sbox_index_find]
            sbox_result = sbox_result + format(val, '04b')
            sb_num += 1

        # I performed the permutation p table to the 32 bits
        p_out = ""
        p_index = 0
        while p_index < 32:
            take_p = P_table[p_index]
            p_out = p_out + sbox_result[take_p - 1]
            p_index = p_index + 1

        # xor the modified right side with the left and swap
        new_right = ""
        left_pos = 0
        while left_pos < 32:
            if left[left_pos] == p_out[left_pos]:
                new_right = new_right + "0"
            else:
                new_right = new_right + "1"
                left_pos = left_pos + 1

            left = right
            right = new_right
            r+=1

    #This is the finall permutation and inverses the IP
    pre_output = right + left# made sure i swapper halves before perm
    cipher_bits = ""
    final_index = 0
    while final_index < 64:
            take_f = F_permutation[final_index]
            cipher_bits = cipher_bits + pre_output[take_f - 1]
            final_index+= 1

    cipher_hex = format(int(cipher_bits, 2), '016X')

    print("\nEncryption done.")
    print("Message plain text:", user_message)
    print("Message hex (used):", message_hex)
    print("Key plain text:", user_key)
    print("Key hex (used):", key_hex)
    print("Cipher (binary):", cipher_bits)
    print("Cipher (hex):", cipher_hex)

    return cipher_bits

decryption()