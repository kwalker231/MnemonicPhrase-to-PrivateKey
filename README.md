# MetaMask Mnemonic to Private Key Converter

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