import mem0
from mem0.embeddings.base import EmbedderBase
# Try to instantiate memory with a dummy config just to see embedder options if possible
# Or just list files in mem0.embeddings
import os, glob
mem0_dir = os.path.dirname(mem0.__file__)
print("Embedders:")
print(os.listdir(os.path.join(mem0_dir, "embeddings")))
