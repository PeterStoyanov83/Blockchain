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

# Create the blockchain

blockchain = Blockchain()

# add to the chain
blockchain.add_block("first block")
blockchain.add_block("second block")
blockchain.add_block("third block")

# dislplay the chain

print("Blockchain:")
for block in blockchain.chain:
    print("Data:", block.data)
    print("Previous hash:", block.prev_hash)
    print("Hash:", block.hash)
    print()
