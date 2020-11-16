import cipher
import binascii

MASTER_KEY = "8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef"
key = binascii.unhexlify(MASTER_KEY)
input_values = ['1122334455667700ffeeddccbbaa9988']


def expand(src):
    dst = src
    dst+=chr(1)
    exp_len = 32 - len(dst) % 32
    dst+=chr(0) * exp_len
    return dst


def unexpand(src):
    dst = src
    while dst[-1] == chr(0):
        del dst[-1]
    del dst[-1]
    return dst


def split(text):
    assert len(text) % 32 == 0 , 'Bad text'
    result = []
    for i in range((len(text) // 32) - 1):
        start = i * 32
        result.append(text[start:start + 32])



def Encrypt_text(text):
    block_bytes = []
    text_in_bytes = bytes(text)
    inputs = []

    #разбить текст на блоки по 32 бита, при необходимости дополнить последний
    #(чем?)
    encrypted_values = execute(lambda block: cipher.encrypt_block(block, key), input_values)
    encrypted_str_blocks = bytes_to_hexStr(encrypted_values)
    return encrypted_str_blocks

def execute(func, inputs):
    actual_output = []
    for i in range(len(inputs)):
        given_input = binascii.unhexlify(inputs[i])    
        actual_output.append(func(given_input))
    return actual_output

def bytes_to_hexStr(inputs):
    outputs = []
    for i in range(len(inputs)):
        outputs.append(binascii.hexlify(inputs[i]))
    return outputs


encrypted_values = execute(lambda block: cipher.encrypt_block(block, key), input_values)
encrypted_str_blocks = bytes_to_hexStr(encrypted_values)

decrypted_values = execute(lambda block: cipher.decrypt_block(block, key), encrypted_str_blocks)
decrypted_str_blocks = bytes_to_hexStr(decrypted_values)

print(f'Input values: {input_values}')
for i in range(len(encrypted_str_blocks)):
    print(f'Ex str: {encrypted_str_blocks[i]}')
for i in range(len(decrypted_str_blocks)):
    print(f'Dec str: {decrypted_str_blocks[i]}')
