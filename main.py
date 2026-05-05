import gdown
import os
import tensorflow as tf

MODEL_PATH = "model.keras"

if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/uc?id=1oCwWNIij0gtoXbnmdehefi4tfO1QGU_U"
    gdown.download(url, MODEL_PATH, quiet=False)

model = tf.keras.models.load_model(MODEL_PATH)