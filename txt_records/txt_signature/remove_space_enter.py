import os

def remove_spaces_and_newlines(file_list):
    for file_name in file_list:
        # 각 파일을 읽어오기
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()

        # 공백과 줄바꿈 제거
        cleaned_content = content.replace(" ", "").replace("\n", "")

        # 결과 파일 이름 설정
        output_file_name = f"{file_name[:-4]}_cleaned.txt"
        output_file_path = os.path.join(os.getcwd(), output_file_name)

        # 결과를 파일에 저장
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        print(f"Processed {file_name}")

# 파일 리스트

file_list = [
    "kyber512_dilithium2_signature",
    "kyber512_dilithium3_signature",
    "kyber512_dilithium5_signature",
    "kyber512_falcon512_signature",
    "kyber512_falcon1024_signature",
    "kyber512_sphincs128f_signature",
    "kyber512_sphincs128s_signature",
    "kyber512_sphincs192f_signature"
]

# 사용 예시
remove_spaces_and_newlines(file_list)

