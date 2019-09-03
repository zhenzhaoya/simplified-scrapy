#!/usr/bin/python
#coding=utf-8
import os,io,hashlib
class HtmlStore:
  _htmls=[]
  _htmlPath='htmls/{}/'
  def __init__(self, name):
    self._htmlPath=self._htmlPath.format(name)
    if(not os.path.exists('htmls/')):
      os.mkdir('htmls/')
    if(not os.path.exists(self._htmlPath)):
      os.mkdir(self._htmlPath)
  def saveHtml(self,url,html):
    self._htmls.append({"url":url,"html":html})
    if(isinstance(url,str)):
      self._saveHtml(url,html)
    else:
      self._saveHtml(url["url"],html)

  def popHtml(self):
    if(len(self._htmls)>0):
      return self._htmls.pop()

  def _saveHtml(self,url,html):
    filename = hashlib.md5(url).hexdigest()+'.htm'   
    file = io.open(self._htmlPath+filename, "w",encoding="utf-8")
    file.write(html)
    file.close()

  def updateState(self,id,state):
    pass