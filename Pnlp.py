#!/usr/bin/env python
# coding: utf-8

# In[4]:


from transformers import pipeline

summarizer = pipeline("summarization", model="Falconsai/text_summarization")

ARTICLE = """ 
 Transformers provides APIs and tools to easily download and train state-of-the-art pretrained models. Using pretrained models can reduce your compute costs, carbon footprint, and save you the time and resources required to train a model from scratch. These models support common tasks in different modalities, such as:
Natural Language Processing: text classification, named entity recognition, question answering, language modeling, summarization, translation, multiple choice, and text generation.
Computer Vision: image classification, object detection, and segmentation.
Audio: automatic speech recognition and audio classification.
Multimodal: table question answering, optical character recognition, information extraction from scanned documents, video classification, and visual question answering.
"""
print(summarizer(ARTICLE, max_length=100, min_length=30, do_sample=False))


# In[ ]:




