
import os
import openai
import creds
import docx

# your OpenAI API KEY
openai.api_key = creds.OPENAI_API_KEY

paperFilePath = "document.docx"

def para2text(p):
  rs = p._element.xpath('.//w:t')
  return u" ".join([r.text for r in rs])

def getText(paperFilePath):
  doc = docx.Document(paperFilePath)
  fullText = []
  for para in doc.paragraphs:
      fullText.append(para2text(para))
  return '\n'.join(fullText)

def askquestion():

  # Extract the document file
  document = getText(paperFilePath)

  # Ask your question
  question = input('Q: ')

  # Prompt is what you feed to the OpenAI to train it together with your question on the last part.
  prompt = document + '\n' + 'Q: ' + question + '\nA:'

  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
  )

  print(f'A: {response.choices[0].text}')
  

if __name__ == '__main__':
  askquestion()