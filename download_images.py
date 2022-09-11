from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ["bird", "bird on bird feeder", "finch", "woodpecker", "cardinal", "pennsylvania bird"]

for kw in keywords:
    response().download(kw, 50)