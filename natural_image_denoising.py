import os
import cv2
import numpy as np
from skimage.metrics import mean_squared_error, structural_similarity, peak_signal_noise_ratio
from skimage.transform import resize
from PIL import Image

'''
def add_noise(img, sigma):
    if img.mode=='L':
        gauss = np.random.normal(scale=sigma, size=(img.height, img.width))
    else:
        gauss = np.random.normal(scale=sigma, size=(img.height, img.width, 3))
    noisy = np.uint8(np.clip(img + gauss, 0, 255))
    return noisy
'''

origin_dir = 'path/to/dir'
noisy_dir = 'path/to/dir'
restore_dir = 'path/to/dir'
ssim_restore_mean = 0
ssim_each_mean = 0
psnr_restore_mean = 0
psnr_each_mean = 0

for i in range(449):
    print(i+1000)
    img = cv2.imread(os.path.join(origin_dir, str(i+1000)+'.jpg'))
    # img_noisy = add_noise(Image.fromarray(img), sigma=20)
    img_noisy = cv2.imread(os.path.join(noisy_dir, str(i+1000)+'.jpg'))
    img_restore = cv2.imread(os.path.join(restore_dir, str(i+1000)+'.jpg'))
    ssim_each = structural_similarity(img[6:-6,6:-6], img_noisy[6:-6,6:-6], multichannel=True)
    assert ssim_each != 0
    ssim_restore = structural_similarity(img[6:-6,6:-6], img_restore, multichannel=True)
    psnr_each = peak_signal_noise_ratio(img[6:-6,6:-6], img_noisy[6:-6,6:-6])
    psnr_restore = peak_signal_noise_ratio(img[6:-6,6:-6], img_restore)
    print('ssim_each: ', ssim_each, '*****' ,'ssim_restore: ', ssim_restore)
    print('psnr_each: ', psnr_each, '*****' ,'psnr_restore: ', psnr_restore)
    ssim_restore_mean += ssim_restore
    ssim_each_mean += ssim_each
    psnr_restore_mean += psnr_restore
    psnr_each_mean += psnr_each
ssim_restore_mean = ssim_restore_mean / 449
ssim_each_mean = ssim_each_mean / 449
psnr_restore_mean = psnr_restore_mean / 449
psnr_each_mean = psnr_each_mean / 449
print('ssim_restore_mean', ssim_restore_mean)
print('ssim_each_mean', ssim_each_mean)
print('psnr_restore_mean', psnr_restore_mean)
print('psnr_each_mean', psnr_each_mean)