#!/usr/bin/python
#coding=utf-8
import json,re,importlib,os
import sys
if sys.version_info.major == 2:
  from core.request_helper import extractHtml
  from core.utils import printInfo
else:
  from .core.request_helper import extractHtml
  from .core.utils import printInfo


class Extracter:
  _models={
    'auto_all':{
      "Type": 2,
      "UrlDomains": "all_domain"
    },
    'auto_lst_obj':{
      "Type": 5,
      "MergeUrl": False
    },
    'auto_lst_url':{
      "Type": 4,
      "MergeUrl": False
    },
    'auto_main_2':{
      "Type": 2
    },
    'auto_main':{
      "Type": 2,
      "UrlDomains": "main_domain"
    },
    'auto_obj':{
      "Type": 3
    }
  }
  def __init__(self):
    try:
      self._iniModels('models/')
    except Exception as err:
        printInfo(err)

  def _iniModels(self, rootdir):
    try:
      if(not os.path.isdir(rootdir)):
        return
      list = os.listdir(rootdir)
      for i in range(0,len(list)):
        name = list[i]
        path = os.path.join(rootdir,name)
        if os.path.isfile(path):
          f = open(path,'r')
          if sys.version_info.major == 2:
            self._models[name[:-5]] = json.loads(f.read().decode('utf-8'))
          else:
            self._models[name[:-5]] = json.loads(f.read())
          f.close()
    except Exception as err:
      printInfo(err)
  def extract(self,url,html,ssp):
    mds = url.get("model")
    if(not mds):
      mds = ssp.models
    models = []
    if(mds):
      for modelName in mds:
        m = self._models.get(modelName)
        if(m):
          models.append(m)
        else:
          printInfo('no model ' + modelName)

    return ssp.extract(url,html,models,mds)
