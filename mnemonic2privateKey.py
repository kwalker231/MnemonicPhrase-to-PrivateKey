from mnemonic import Mnemonic
from bip32utils import BIP32Key

# This is an example seed phrase
#mnemonicPhrase = "one two three four five six seven eight nine ten eleven twelve"

#Enter Your Mnemonic Phrase Here
mnemonicPhrase = "one two three four five six seven eight nine ten eleven twelve" 

passphrase = "" #empty

#create Mnemonic instance and generate seed from mnemonic phrase
mnemo = Mnemonic("english")
seed = mnemo.to_seed(mnemonicPhrase, passphrase)

#create BIP32Key instance from seed
bip32Key = BIP32Key.fromEntropy(seed)

#generate child key from BIP-44 path
coin_type = 60 #ethereum: coin_type =60
account_index = 0  #from 0 -> increasing manner
change = 0  #Constant 0 is for external chain, constant 1 for internal chain 
address_index = 0  #from 0 -> increasing manner

#generate child private key step by step
# m/44' (BIP-44 purpose')
childKey = bip32Key.ChildKey(44 | 0x80000000) #hardened derivation
# m/44'/60' (BIP-44 coin_type')
childKey = childKey.ChildKey(coin_type | 0x80000000) #hardened derivation
# m/44'/60'/0' (BIP-44 account')
childKey = childKey.ChildKey(account_index | 0x80000000) #hardened derivation
# m/44'/60'/0'/0 (BIP-44 change)
childKey = childKey.ChildKey(change)
# m/44'/60'/0'/0/0 (BIP-44 address_index)
childKey = childKey.ChildKey(address_index)

print(f"Mnemonic Phrase: {mnemonicPhrase}")

#generate master private key's WIF（Wallet Import Format）
masterPrivateKeyWif = bip32Key.WalletImportFormat()
print(f"Master Private Key (WIF): {masterPrivateKeyWif}")

#generate child private key
# BIP-44 path: m / 44' / coin_type' / account' / change / address_index
childPrivateKey = childKey.PrivateKey()
childPrivateKey = childPrivateKey.hex()
print(f"Child Private Key (acc1): {childPrivateKey}")