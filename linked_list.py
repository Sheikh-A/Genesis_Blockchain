import hashlib
class Block:
    def __init__(self, index, timestamp, content, previous_hash):
      self.index = index
      self.timestamp = timestamp
      self.content = content
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
      sha = hashlib.sha256()
      sha.update(str(self.index).encode('utf-8') +
                 str(self.timestamp).encode('utf-8') +
                 str(self.content).encode('utf-8') +
                 str(self.previous_hash).encode('utf-8'))
      return sha.hexdigest()

M4BlockChain = []

from datetime import datetime
def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")

M4BlockChain.append(create_genesis_block())


# write a function `next_block` to generate a block
def next_block(last_block):
    blockchain_index = last_block.index + 1
    #add timestamp
    next_block_timestamp = datetime.now()
    #generate content
    next_block_content = "Block Number #: ",  str(blockchain_index)
    previous_blockchain_hash = last_block.hash

    #define the new block here
    newest_block = Block(blockchain_index, next_block_timestamp, next_block_content, previous_blockchain_hash)
    #Test Print function
    #print("NEW BLOCK GENERATED: ", newest_block, blockchain_index)

    return newest_block


# append 5 blocks to the blockchain
def app_five(block_list):
  appendblockvalue = 5

  for i in range(appendblockvalue):
    #get length
    blockchain_length = len(block_list)
    #adding location
    terminal_block = block_list[blockchain_length-1]
    #append to linked list
    block_list.append(next_block(terminal_block))

  #print(block_list)
  # return block_list


# M4BlockChain.append(app_five(M4BlockChain))
# print(len(M4BlockChain))
# print("first block: ", M4BlockChain[0].index)
# print("second block: ", M4BlockChain[1].index)
# print("third block: ", M4BlockChain[2].index)
# print("fourth block: ", M4BlockChain[3].index)
# print("fifth block: ", M4BlockChain[4].index)
# print("fifth block: ", M4BlockChain[5].index)
