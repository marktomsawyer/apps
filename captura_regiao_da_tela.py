from PIL import ImageGrab
regiao = (300, 300, 600, 600)
screenshot = ImageGrab.grab(regiao)
screenshot.save("screenshot_region.jpg")