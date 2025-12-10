from cs import key

def encryption():
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


    #Here I took the user input turned it into hex characters then binary

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


#Expansion table
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
    
    #Here I perform the first perm and divide into left and right side
    key_bits56=""
    index=0
    while index<56:
        pos3= PC1[index]
        key_bits56= key_bits56+key_bits[pos3-1]
        index +=1

        half=len(key_bits56)//2
        left_key=key_bits56[0:half]
        right_key=key_bits56[half:]

        print("Left key: ",left_key)
        print("Right key: ")


    #Here I perform the shifts accordingly
        round_key=[]
        round_number=1
        while round_number<=16:
            if round_number==1 or round_number==2 or round_number==9 or round_number==16:
                shifts=1
            else:
                shifts=2

    shifts_count=0
    while shifts_count < shifts:
        fsb_left=left_key[0]
        new_left=""
        left_index=1
        while left_index<len(left_key):
            new_left= new_left + left_key[left_index]
            left_index = left_index + 1
            left_key = new_left + fsb_left
            fsb_right = right_key[0]
            new_right = ""
            right_index = 1
    while right_index < len(right_key):
        new_right = new_right + right_key[right_index]
        right_index += 1
        right_key = new_right + fsb_right

        shift_count += 1

        combined_key = left_key + right_key

    subkey = ""
    pc2_index = 0
    while pc2_index < 48:
        pick_pos = PC2[pc2]
        subkey = subkey + combined_key[pick_pos - 1]
        pc2+=1

    round_key.append(subkey)
    round_number+=1


    permuted = ""
    perm_index = 0
    while perm_index < 64:
        take_pos = IP[perm_index]
        permuted = permuted + message_bits[take_pos - 1]
        perm_index+=1

    left = permuted[0:32]
    right = permuted[32:64]

    round_counter = 0
    while round_counter < 16:

        expanded_right = ""
        expanded_index = 0
        while expanded_index < 48:
            take_e = E_table[expanded_index]
            expanded_right = expanded_right + right[take_e - 1]
            expanded_index = expanded_index + 1


        round_key = round_key[round_counter]
        xored= ""
        xored_index  = 0
        while xored_index < 48:
            if expanded_right[xored_index] == round_key[xored_index]:
                xored = xored + "0"
        else:
            xored = xored + "1"
            xored_index = xored_index + 1


        sbox_result = ""
        sb_num = 0
        while sb_num < 8:
            start = sb_num * 6
            block6 = xored[start:start+6]
            row_bits = block6[0] + block6[5]
            col_bits = block6[1:5]
            row_val = int(row_bits, 2)
            col_val = int(col_bits, 2)
            idx2 = row_val * 16 + col_val
            box = S_BOXES[sb_num]
            val = box[idx2]
            sbox_result = sbox_result + format(val, '04b')
            sb_num = sb_num + 1


        p_out = ""
        p_index = 0
        while p_index < 32:
            take_p =  P_table[p_index]
            p_out = p_out + sbox_result[take_p - 1]
            p_index = p_index + 1


        new_right = ""
        left_pos = 0
        while left_pos < 32:
            if left[left_pos] == p_out[left_pos]:
                new_right = new_right + "0"
            else:
                new_right = new_right + "1"
            left_pos+=1
            left = right
            right = new_right
            r+=1


        pre_output = right + left
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

encryption()
