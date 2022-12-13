img = imread("FiberDataset_3\PNGImages\image1.png");
figure
imshow(img)
BW = imbinarize(img);

[B,L] = bwboundaries(BW);


im = label2rgb(L, @gray, [.5 .5 .5]);

r = im(:,:,1);
g = im(:,:,2);
b = im(:,:,3);

Mask = r == 128 & g == 128 & b == 128; 

figure,imshow(Mask)

figure,imshow(im)


r(Mask) = 0;
g(Mask) = 0;
b(Mask) = 0;

rgbImage2 = cat(3, r, g, b);
figure
imshow(rgbImage2);
imwrite(rgbImage2,"FiberDataset_3\PedMasks\image1_mask.png")
