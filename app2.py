import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
             'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 검색창 
va1 = st.text_input("무슨 이미지를 찾으시나요? ")

# 입력창에서 데이터를 받아서 
st.text(f"{va1}를 입력하셨습니다.")

# 해당 문자열이 일치하는 이미지를 화면에 출력해 보세요.
if va1 == '짱구는 못말려':
    st.image(img_list[0])
elif va1 == '몬스터':
    st.image(img_list[1])
elif va1 == '릭앤모리':
    st.image(img_list[2])

# 이미지 링크를 다운로드 받는 버튼 생성하기
# 모르겠다요... 


#강사님
# title = st.text_input('검색하실 애니메이션을 입력하세요')

# for ani_ in ani_list:
    # if title in ani_:
        #ani_list에서 특정 문자열을 포함한 인덱스
        #img_idx = ani_list.index(ani_)

# if title != "":
    # st.image(img_list[img_idx])

# 중단점 