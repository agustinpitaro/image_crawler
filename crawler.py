from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

#define search params:
search_params = {
    "keywords": "yerba rosamonte",
            "limit": 15,
            "size": "large",
            "print_urls": True,
            "output_directory": 'D:\Database 3000'
}

absolute_image_paths = response.download(search_params)
print(absolute_image_paths)
