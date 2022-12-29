# Import the necessary libraries
import hashlib
import datetime

# Define the Blockchain class

class Blockchain:

  def __init__(self):
    self.chain = []
    self.current_nfts = {}
    self.nfts = {}

  def new_block(self, proof, previous_hash):
    block = {
      'index': len(self.chain) + 1,
      'timestamp': datetime.datetime.now(),
      'proof': proof,
      'previous_hash': previous_hash,
      'nfts': self.current_nfts
    }
    self.current_nfts = {}
    self.chain.append(block)
    return block

  def new_nft(self, nft_id, owner, metadata):
    self.current_nfts[nft_id] = {
      'owner': owner,
      'metadata': metadata
    }
    self.nfts[nft_id] = {
      'owner': owner,
      'metadata': metadata
    }
    return True

  def get_block_containing_nft(self, nft_id):
    for block in self.chain:
      for nft_id in block['nfts']:
        if nft_id in block['nfts']:
          return block
    return None

  @staticmethod
  def hash(block):
    encoded_block = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(encoded_block).hexdigest()

  @property
  def last_block(self):
    return self.chain[-1]

# Define a function that takes in a NFT and returns the metadata for that NFT
# without revealing any of the financial transaction details

def get_nft_metadata(blockchain, nft_id):

  # Get the block that contains the NFT
  block = blockchain.get_block_containing_nft(nft_id)

  # Extract the NFT from the block and return its metadata
  if block:
    nft = block['nfts'][nft_id]
    return nft['metadata']
  return None

# Create a new Blockchain object
blockchain = Blockchain()

# Add some blocks and NFTs to the blockchain
blockchain.new_block(proof=123, previous_hash='abc')
blockchain.new_nft(nft_id=1, owner='Alice', metadata={'name': 'Cat', 'color': 'black'})
blockchain.new_block(proof=456, previous_hash='def')
blockchain.new_nft(nft_id=2, owner='Bob', metadata={'name': 'Dog', 'color': 'brown'})

# Example usage: get the metadata for NFT with ID 1
metadata = get_nft_metadata(blockchain, 1)
print(metadata)  # Output: {'name': 'Cat', 'color': 'black'}

# Example usage: get the metadata for NFT with ID 2
