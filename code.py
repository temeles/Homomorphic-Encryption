from phe import paillier
public_key, private_key = paillier.generate_paillier_keypair()
secret_num = int(input("Enter number"))
secret_num2 = int(input("Enter number"))
secret_num3 = int(input("Enter number"))
encrypt1 = public_key.encrypt(secret_num)
encrypt2 = public_key.encrypt(secret_num2)
encrypt3 = public_key.encrypt(secret_num3)
encrypted_nums = [encrypt1, encrypt2, encrypt3]
import json
enc_public_key = {}
enc_public_key ['public_key'] = {'g': public_key.g, 'n' :public_key.n} #storing a value of a g into g and a value of n into n, and into public key 
enc_public_key ['values'] = [(str(x.ciphertext()), x.exponent) for x in encrypted_nums]
serialised = json.dumps(enc_public_key)#stores public key and values and encryption into variable serialised
f = open('file.txt', "w") #w = writing                     above is client   message.encode() > serialized.encode()                                                                                                                                                                                                                                               
f.write(serialised) #overwrite file with serialised code  #socket programming
f.close() 
f= open('file.txt', 'r') #'r' = read, open file to read
print(f.read()) #show user file
rec_dict = json.loads(serialised) #set equal to file     below is server 
pk = rec_dict['public_key'] #return public key to numbers 
public_key_rec = paillier.PaillierPublicKey(n=int(pk['n'])) #assign integer to deserialise values of n and g 
enc_nums_rec = [paillier.EncryptedNumber(public_key_rec, int(x[0]), int(x[1])) for x in rec_dict['values']] #deseralise values
a = 3
a2 = 5
a3 = 6
b = 0
y = a*encrypt1 + a2 * encrypt2 + a3*encrypt3 +b
r = [y]   
enc_public_key2 = {}
enc_public_key2['public_key'] = {'g': public_key.g, 'n' :public_key.n} #storing a value of a g into g and a value of n into n, and into public key 
enc_public_key2 ['values'] = [(str(x.ciphertext()), x.exponent) for x in r]
serialised2 = json.dumps(enc_public_key2)   # end of server
f = open('testing.txt', "w") #w = writing        #socket programming                                                                                                                                                                                                                                                               
f.write(serialised2) #overwrite file with serialised code
f.close() 
f= open('testing.txt', 'r')
print(f.read()) #show user file
rec_dict2 = json.loads(serialised2) #set equal to file   #client 
pk2 = rec_dict2['public_key'] #return public key to numbers 
public_key_rec2 = paillier.PaillierPublicKey(n=int(pk['n'])) #deserialise values of n and g 
enc_num_rec2 = [paillier.EncryptedNumber(public_key_rec2, int(x[0]), int(x[1])) for x in rec_dict2['values']] #deseralise values
m = private_key.decrypt(enc_num_rec2[0])#acess first element in 0     for example x is list and [0] calls first in list
print(m)


