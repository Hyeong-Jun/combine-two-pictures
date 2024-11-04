from PIL import Image, ImageEnhance

# 자료 사진 불러오기
background = Image.open('background.jpg').convert("RGBA")
player = Image.open('baseball player.jpeg').convert("RGBA")

# 배경 이미지를 선수 이미지 크기에 맞게 조정
background = background.resize(player.size, Image.Resampling.LANCZOS)

# 크기 조정된 배경 이미지의 선명도 향상
enhancer = ImageEnhance.Sharpness(background)
background = enhancer.enhance(2.0)  # 선명도를 2.0 배로 증가

# 단색 배경(예: 흰색)으로 새 이미지 생성
solid_background = Image.new("RGBA", background.size, (255, 255, 255, 255))

# 크기 조정된 배경 이미지를 단색 배경에 붙여넣기
solid_background.paste(background, (0, 0), background)

# 선수 이미지를 결합된 이미지에 붙여넣기
solid_background.paste(player, (0, 0), player)

# 결과 저장!
solid_background.save('combined_image.png')

