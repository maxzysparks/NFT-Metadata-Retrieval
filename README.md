# NFT-Metadata-Retrieval
This code defines a Blockchain class in Python and a function get_nft_metadata that can be used to retrieve the metadata for a non-fungible token (NFT) from an instance of the Blockchain class.

The Blockchain class has several methods:

__init__: Initializes a new instance of the Blockchain class, setting up the necessary instance variables.
new_block: Creates a new block and adds it to the end of the blockchain.
new_nft: Creates a new NFT and adds it to the current block in the blockchain.
get_block_containing_nft: Returns the block in the blockchain that contains the NFT with the given ID.
hash: Returns the SHA-256 hash of a given block, encoded as a hexadecimal string.
last_block: Returns the last block in the blockchain.
The get_nft_metadata function takes in an instance of the Blockchain class and an nft_id as arguments, and returns the metadata for the NFT with the given ID from the blockchain. It does this by using the get_block_containing_nft method of the Blockchain object to get the block that contains the NFT with the given nft_id, and then extracting the NFT from the block and returning its metadata.

Finally, the code creates a new instance of the Blockchain class and adds some blocks and NFTs to it, and then demonstrates how to use the get_nft_metadata function to retrieve the metadata for a specific NFT.
However, it's worth noting that the code makes use of several libraries that are not included in the Python standard library. In particular, it imports the hashlib library, which is used to compute the SHA-256 hash of a block, and the datetime library, which is used to get the current date and time when creating a new block. These libraries will need to be imported at the beginning of the code in order for it to run properly.

Additionally, the code assumes that the json library is available and uses the json.dumps function to encode a block as a JSON string. This library will also need to be imported in order for the code to run properly.
