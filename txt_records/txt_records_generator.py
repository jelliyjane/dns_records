import os

def process_directory(file_list):
    total_chunks = 0

    for file_name in file_list:
        # 각 파일을 읽어오기
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()

        # 230바이트씩 나누기
        chunks = [content[i:i + 230] for i in range(0, len(content), 230)]

        # 앞 뒤로 큰 따옴표와 빈 칸 추가
        formatted_chunks = [' " {} " '.format(chunk) for chunk in chunks]

        # 결과 파일 이름 설정
        output_file_name = f"{file_name[:-12]}_output.txt"
        output_file_path = os.path.join(os.getcwd(), output_file_name)

        # 결과를 파일에 저장
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(''.join(formatted_chunks))

        total_chunks += len(chunks)
        print(f"Processed {file_name}: Total chunks: {total_chunks}")

# 파일 리스트 정의
"""
file_list = [
    "txt_signature/kyber512_dilithium2_signa_cleaned.txt",
    "txt_signature/kyber512_dilithium3_signa_cleaned.txt",
    "txt_signature/kyber512_dilithium5_signa_cleaned.txt",
    "txt_signature/kyber512_falcon512_signa_cleaned.txt",
    "txt_signature/kyber512_falcon1024_signa_cleaned.txt",
    "txt_signature/kyber512_sphincs128f_signa_cleaned.txt",
    "txt_signature/kyber512_sphincs128s_signa_cleaned.txt",
    "txt_signature/kyber512_sphincs192f_signa_cleaned.txt"
]
"""

file_list = [
'kyber512'
]

# 사용 예시
process_directory(file_list)
