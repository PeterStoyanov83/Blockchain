import hashlib


class Block:

    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()


class Blockchain:

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    # create the 1st block in the blockchain

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    # create method adding blocks to the chain

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(data, prev_block.hash)
        self.chain.append(new_block)


# test the chain

# 1 Create the blockchain

blockchain = Blockchain()

# 2 add to the chain
blockchain.add_block("first block")
blockchain.add_block("second block")
blockchain.add_block("third block")

# 3 show the chain

print("Blockchain:")
for block in blockchain.chain:
    print("Data:", block.data)
    print("Previous hash:", block.prev_hash)
    print("Hash:", block.hash)
    print()


''' 
this outputs : 

Blockchain:
Data: Genesis Block
Previous hash: 0
Hash: 89eb0ac031a63d2421cd05a2fbe41f3ea35f5c3712ca839cbf6b85c4ee07b7a3

Data: first block
Previous hash: 89eb0ac031a63d2421cd05a2fbe41f3ea35f5c3712ca839cbf6b85c4ee07b7a3
Hash: 2af7909ca08f18facc556624b02e1a5c683bb0f557137b1ef7e0028fc457715c

Data: second block
Previous hash: 2af7909ca08f18facc556624b02e1a5c683bb0f557137b1ef7e0028fc457715c
Hash: d387a3f3e5c0aebd3847c2dde0a248ddb1fa8f04fe6ff99e9ce7e60fdbcd9c3f

Data: third block
Previous hash: d387a3f3e5c0aebd3847c2dde0a248ddb1fa8f04fe6ff99e9ce7e60fdbcd9c3f
Hash: a4781a098e6c0c2f52a15916ef2dd45a39c488e47ed8eab672ceecadbb74e9f1


Process finished with exit code 0
'''
