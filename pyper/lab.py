import os
from pyper import Piper



os.environ["ORT_DYLIB_PATH"] = r"D:\onnxruntime_libs\x86\onnxruntime.dll"
os.environ["PIPER_ESPEAKNG_DATA_DIRECTORY"] = r"D:\projects\blindpandas\piper-rs\deps\windows\espeak-ng-build"


p = Piper(
    r"D:\Piper_TTS_Voices\voices\voice-en-us-libritts-high\en-us-libritts-high.onnx.json",
    r"D:\Piper_TTS_Voices\voices\voice-en-us-libritts-high\en-us-libritts-high.onnx"
)

print(p.synthesize("hello", 1, 1, 1, None))