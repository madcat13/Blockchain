#############################################################
#This project is written in Object-Oriented approach and
#is a simple implementation of a blockchain.

# The program performs following actions:
#  -creates a block and generates hash for it
#  -creates new block based on the hash in previous block
#  -adds proof(proof of contract) to each block
#  -enables user input data to be added to blockchain
#############################################################

#import libraries
from hashlib import sha256
import time
from random import randrange

#class constructor for the block
class Block:
    def __init__ (self,timestamp, data, previous_hash = ' '):
        self.timestamp = timestamp
        self.data = data
        self.proof = self.get_proof()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
     
    def calculate_hash(self):
        # receive  timestamp, data and previous hash from the block as a string
        # hash with SHA256 encryption
        return sha256((str(self.timestamp) 
                       + str(self.data) + 
                       str(self.previous_hash))
                      #turn string variables into unicode(encode())for hashing
                      #then translate unicode into a hexidecimal string (hexdigest())
                      .encode()).hexdigest()
    #get proof of contract(a random integer to prove a proof of concept)
    def get_proof(self):
        proof=randrange(1,1000000)
        return proof
        
#class constructor for the blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.generate_genesis_block()]
    #genesis block is the first block of the blockchain
    def generate_genesis_block(self):
        return Block(time.ctime(), "Genesis Block", "0")

    def mineBlock(self, data):
        #get parameters for the new block 
        new_block = Block(time.ctime(), data, self.chain[-1].hash)  
        # mine new block to be added to the most recent block in chain
        self.chain.append(new_block)
        print("\n\n ===================== !!! New Block mined successfully !!! ===================== ")

    def print_blockchain(self):
        for i in range(len(self.chain)):
            print("\n----------------------------------- Block ", i ,"-----------------------------------\n"
                  "\n timestamp = ",\
                    self.chain[i].timestamp
                  ,"\n data = ", \
                    self.chain[i].data
                  , "\n previous hash = ",\
                    self.chain[i].previous_hash
                  , "\n hash = ",\
                    self.chain[i].hash
                  ,"\n proof = ", \
                    self.chain[i].proof)
            
#function to get user input to be added to block as a transaction
def get_user_input():
    data=input()
    #check that input is not empty
    if data == '':
        print("Please enter text to be added to block")
        return get_user_input()
    else:
        return data

#function to add new block to the chain
def add_block():
    #get user input
    data=get_user_input()
    #add user input to block as a transaction
    Mcoin.mineBlock(data)
    #print mined block and the chain
    Mcoin.print_blockchain()
    
#initiate blockchain
Mcoin = Blockchain()
#call the function to add blocks to the chain
add_block()
