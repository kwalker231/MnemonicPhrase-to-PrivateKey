# Mnemonic to Private Key Converter

This Python script is designed to convert a MetaMask mnemonic phrase into private keys. It follows the BIP-32 standard for hierarchical deterministic (HD) key generation.

## Features

- Converts a 12-word mnemonic phrase to a seed.
- Derives the master private key from the seed.
- Generates child private keys based on the BIP-44 path.

## Prerequisites

- Python 3.11
- `mnemonic`
- `bip32utils`

You can install the required libraries using pip:

```bash
pip install mnemonic bip32utils
```

## Usage

1. Place your 12-word mnemonic phrase into the mnemonic_phrase variable in the script.
2. Run the script.
3. The script will output the master private key and child private keys for the specified BIP-44 path

## Algorithm and Standards

This script is based on the algorithm outlined in the MetaMask key-tree library, which provides an interface over SLIP-10, BIP-32, and BIP-44 key derivation paths. For more information, please refer to the [MetaMask key-tree repository](https://github.com/MetaMask/key-tree/tree/main).

The BIP-44 path levels, which define the structure of the derivation path, can be found in the official Bitcoin Improvement Proposals repository: [BIP-0044](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki).

## Disclaimer

Please use this script responsibly. The security of your private keys is crucial. Always keep your mnemonic phrase and private keys secure and private. The author is not responsible for any loss of funds or security breaches caused by the use of this script.