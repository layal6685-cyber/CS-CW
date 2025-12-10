shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1] # For me to know the shifts


#First choice permutaion
pc1 = [
57,49,41,33,25,17,9,
1,58,50,42,34,26,18,
10,2,59,51,43,35,27,
19,11,3,60,52,44,36,
63,55,47,39,31,23,15,
7,62,54,46,38,30,22,
14,6,61,53,45,37,29,
21,13,5,28,20,12,4
]


#Second choice permutation
pc2 = [
14,17,11,24,1,5,
3,28,15,6,21,10,
23,19,12,4,26,8,
16,7,27,20,13,2,
41,52,31,37,47,55,
30,40,51,45,33,48,
44,49,39,56,34,53,
46,42,50,36,29,32
]

def key(user_key=None):
    if user_key is None:
        user_key=input("Please enter key wiht maximun 8 characters: ")
    binary_key=""
    for char in user_key:
        binary_key+= format(ord(char),"08b")
    print("Binary message is: ", binary_key)

    if len(binary_key)!=64:
        print("Key must be 64 bits")
        return None
    
    pos=0
    while pos < 64:
        if binary_key[pos]!="0" and binary_key[pos]!="1":
            print("Key did not turn into binary")
            return None
        pos+=1


    # Here I basically took the key from the user and ensured it turned into 64 bits

    new_bits=""
    index=0
    while index < 56:
        chosen_index=pc1[index]
        bit_from_key= binary_key[chosen_index-1]
        new_bits=new_bits+bit_from_key
        index+=1

    half=len(new_bits)//2
    C0=new_bits[0:half]
    D0=new_bits[half:]
    print("C0=: ",C0,"D0=",D0)

    #Here I performed the first choice permutation and skipped the 8 bits then made half C and D

    round_keys=[]
    round_number=1
    while round_number<= 16:
        if round_number==1 or round_number==2 or round_number==9 or round_number==16:
            shifts_number=1
        else:
            shifts_number=2

        shift_counter=0
        while shift_counter < shifts_number:
            first_bit=C0[0]
            new_C=""
            C_pos=1
            while C_pos < len(C0):
                new_C=new_C + C0[C_pos]
                C_pos+=1
            C0=new_C + first_bit

    #Here I basically ensured that every round has its correct shift

            
            first_bitD=D0[0]
            new_D=""
            D_pos=1
            while D_pos < len(D0):
                new_D= new_D + D0[D_pos]
                D_pos+=1
            D0=new_D + first_bitD

            shift_counter+=1
  
        
        #Here I am perforimg the second choice Permutation after the shifts and combining C and C to make it complete Perm
        combined = C0 + D0
        subkey_bits=""
        pc2_index=0
        while pc2_index < 48:
            chosen_index=pc2[pc2_index]
            if chosen_index < 1 or chosen_index > len(combined):
                print(f"There is an Error pc2 in : [{pc2_index}]={chosen_index} is out of range for combined length {len(combined)}")
                return None
            chosen_bit=combined[chosen_index-1]
            subkey_bits=subkey_bits+chosen_bit
            pc2_index+=1

        round_keys.append(subkey_bits)
        round_number+=1

    print("Round keys are: ", round_keys)
    return round_keys

key()