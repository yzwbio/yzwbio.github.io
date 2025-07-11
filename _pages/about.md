---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hello there! 🙋🏼 I am Yizheng Wang (王一争), a Ph.D. candidate at the University of Electronic Science and Technology of China.

I obtained my bachelor's degree 🎓 in Computer Science and Technology from the &nbsp;<img src='./images/ysu.jpg' style='height: 1.5em;'>&nbsp; [School of Information Science and Engineering](http://ise.ysu.edu.cn), [Yanshan University](http://www.ysu.edu.cn) (燕山大学，信息科学与工程学院). 

I am pursuing my Ph.D. degree 🎓 through a combined Master’s and Doctoral program (硕博连读) at the &nbsp;<img src='./images/iffs.jpg' style='height: 1.5em;'>&nbsp; [Institute of Fundamental and Frontier Sciences](https://www.iffs.uestc.edu.cn/),&nbsp;<img src='./images/uestc.jpg' style='height: 1.5em;'>&nbsp; [University of Electronic Science and Technology of China](https://www.uestc.edu.cn) (电子科技大学，基础与前沿研究院), majoring in Computer Science and Technology. 

I am part of a joint training program (联合培养) at the &nbsp;<img src='./images/ydri.jpg' style='height: 1.5em;'>&nbsp; [Yangtze Delta Region Institute (Quzhou)](http://ydri.uestc.edu.cn), &nbsp;<img src='./images/uestc.jpg' style='height: 1.5em;'>&nbsp; [University of Electronic Science and Technology of China](https://www.uestc.edu.cn) (电子科技大学，长三角研究院).

I currently conduct research in the [Malab](http://123.57.240.48/forum.php?mod=viewthread&tid=8672) laboratory 🔬 under the supervision of [Prof. Dr. Quan Zou](http://lab.malab.cn/~zq/) (邹权教授). My main research areas are machine learning 🤖 and computational biology 🧬, with several publications in SCI-indexed journals. <a href='https://scholar.google.com/citations?user=NEWRm1gAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

# 📒 Research Interests
### 🤖 Machine learning
- Artificial Intelligence (人工智能)
- Large Language Model (大语言模型)
- Support bio-sequence machine (支持生物序列机)
- Support bio-sequence neural network (支持生物序列神经网络)

### 🧬 Computational biology 
- Biological sequence analysis (生物序列分析)
- Biological interactions prediction (生物关联预测)
- Multiple sequence alignment (多序列比对)
- Therapeutic peptide design (治疗肽设计)
- Phylogenetic tree construction (系统发生树构建)

# 🔥 News
- *2025.05.13*: My paper has been recognized by <img src='images/Clarivate.jpg' style='height: 0.95em;'> as both a 🏆 Highly Cited Paper and a 🔥 Hot Paper! 
- *2024.12.27*: I have been awarded the CSC Scholarship for the joint training program abroad! ✈️🎉
- *2024.10.07*: My new paper has been accepted by the CCF A journal *SCIENCE CHINA Information Sciences*! 📑🎉
- *2024.03.17*: My new personal homepage has been released. 🌐🎉

# 📝 Projects

<!------------------------------------------------------------------------------>
<div class='paper-box'>
  <div class='paper-box-image'>
      <div class="badge">Perform Experiments</div>
      <img src='images/amp.jpg' alt="sym" width="100%">
  </div>
  <div class='paper-box-text' markdown="1">

(1) [Rational De Novo Design of Multifunctional Therapeutic Peptides Guided by Support Bio-sequence](#)

***Yizheng Wang**, Yijie Ding\*, Quan Zou\**

  </div>
</div>
<!------------------------------------------------------------------------------>


<!------------------------------------------------------------------------------>
<div class='paper-box'>
  <div class='paper-box-image'>
      <div class="badge">Under Review</div>
      <img src='images/SBNN.jpg' alt="sym" width="100%">
  </div>
  <div class='paper-box-text' markdown="1">

(2) [Support Bio-Sequence-Guided Bio-Language Modeling of Nucleic Acids for Epigenetic Modification Prediction](#)

***Yizheng Wang**, Pinglu Zhang, Yi Ding, Wenyu Zhang, Yanming Wei, Yijie Ding\*, Quan Zou\**

  </div>
</div>
<!------------------------------------------------------------------------------>



<!------------------------------------------------------------------------------>
<div class='paper-box'>
  <div class='paper-box-image'>
      <div class="badge">Perform Experiments</div>
      <img src='images/JianMu.jpg' alt="sym" width="100%">
  </div>
  <div class='paper-box-text' markdown="1">

(3) [JianMu*: Fast Phylogenetic Tree Construction via Siamese Bio-sequence Language Model-based Metric Learning](#)

***Yizheng Wang**, Yijie Ding\*, Quan Zou\**

<br>
<br>
<br>

<p style="font-size: 0.85em; font-style: italic;">*In ancient Chinese mythology, <strong>JianMu(建木)</strong> is a sacred tree, a bridge connecting heaven and earth. In biology, the phylogenetic tree is a bridge connecting genes and evolution. Thus, we chose the name <strong>JianMu</strong> for our model, highlighting its role in uncovering species relationships.</p>


  </div>
</div>
<!------------------------------------------------------------------------------>



<!------------------------------------------------------------------------------>
<div class='paper-box'>
  <div class='paper-box-image'>
      <div class="badge">Perform Experiments</div>
      <img src='images/hckdm.jpg' alt="sym" width="100%">
  </div>
  <div class='paper-box-text' markdown="1">

(4) [SSM: Support Subsequence Machine](#)

***Yizheng Wang**, Yijie Ding\*, Quan Zou\**

🌐 [Website](http://lab.malab.cn/soft/SSM/)

  </div>
</div>
<!------------------------------------------------------------------------------>



<!------------------------------------------------------------------------------>
<div class='paper-box'>
  <div class='paper-box-image'>
      <div class="badge_red">CCF A</div>
      <img src='images/SBSMPRO.jpg' alt="sym" width="100%">
  </div>
  <div class='paper-box-text' markdown="1">

(5) [SBSM-Pro: Support Bio-sequence Machine for Proteins](https://www.sciengine.com/SCIS/doi/10.1007/s11432-024-4171-9)

***Yizheng Wang**, Yixiao Zhai, Yijie Ding\*, Quan Zou\**

*SCIENCE CHINA Information Sciences, [CCF A](https://www.ccf.org.cn/Academic_Evaluation/Cross_Compre_Emerging/), [CAAI A](https://www.caai.cn/index.php?s=/home/article/detail/id/4024.html), IF2024=7.300*, 中科院1区top

<img src='images/Clarivate.jpg' style='height: 0.95em;'> 🏆 [Highly Cited Paper](https://yzwbio.github.io/_pages/hotpaper.html) (高被引论文) 🔥 [Hot Paper](https://yzwbio.github.io/_pages/hotpaper.html) (热点论文) 


🌐 [Website](http://lab.malab.cn/soft/SBSM-Pro/)

  </div>
</div>
<!------------------------------------------------------------------------------>



<!------------------------------------------------------------------------------>
<div class='paper-box'>
  <div class='paper-box-image'>
      <div class="badge">CCF B</div>
      <img src='images/HSICLP.jpg' alt="sym" width="100%">
  </div>
  <div class='paper-box-text' markdown="1">

(6) [Identification of human microRNA-disease association via low-rank approximation-based link propagation and multiple kernel learning](https://journal.hep.com.cn/fcs/EN/10.1007/s11704-023-2490-5)

***Yizheng Wang**, Xin Zhang, Ying Ju, Qing Liu, Quan Zou, Yazhou Zhang, Yijie Ding\*, Ying Zhang\**

*Frontiers of Computer Science, [CCF B](https://www.ccf.org.cn/Academic_Evaluation/Cross_Compre_Emerging/), [CAAI B](https://www.caai.cn/index.php?s=/home/article/detail/id/4024.html), IF2022=4.200*, 中科院2区

  </div>
</div>
<!------------------------------------------------------------------------------>



<!------------------------------------------------------------------------------>
<div class='paper-box'>
  <div class='paper-box-image'>
      <div class="badge">JCR Q2</div>
      <img src='images/et.jpg' alt="sym" width="100%">
  </div>
  <div class='paper-box-text' markdown="1">
    
(7) [ET-MSF: A model stacking framework to identify electron transport proteins](https://www.imrpress.com/journal/FBL/27/1/10.31083/j.fbl2701012/htm)

***Yizheng Wang**, Qingfeng Pan\*, Xiaobin Liu\*, Yijie Ding\**

*Frontiers in Bioscience-Landmark, JCRQ2, IF2021=4.009*

  </div>
</div>
<!------------------------------------------------------------------------------>


<!------------------------------------------------------------------------------>
<div class='paper-box'>
  <div class='paper-box-image'>
      <div class="badge">CCF C</div>
      <img src='images/XGBoost.jpg' alt="sym" width="100%">
  </div>
  <div class='paper-box-text' markdown="1">
    
(8) [SeqAlignXGBoost: Sequence Alignment and Feature Selection for m1A Modification Site Identification](#)

***Yizheng Wang**, Yijie Ding\*, Quan Zou\**

*2025 International Conference On Intelligent Computing (ICIC2025), CCF C*

  </div>
</div>
<!------------------------------------------------------------------------------>

- (9) [TPMA: A two pointers meta-alignment tool to ensemble different multiple nucleic acid sequence alignments](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011988), *Yixiao Zhai, Jiannan Chao, **Yizheng Wang**, Pinglu Zhang, Furong Tang\*, Quan Zou\*. PLOS Computational Biology, Q1, IF2024=3.800*

- (10) [A survey on multi-view fusion for predicting links in biomedical bipartite networks: Methods and applications](https://www.sciencedirect.com/science/article/pii/S1566253524006729), *Yuqing Qian, **Yizheng Wang**, Junkai Liu, Quan Zou\*, Yijie Ding\*. Information Fusion, Q1, IF2024=14.700*

- (11) [Application of Artificial Intelligence in Drug-Target Interactions Prediction: A Review](https://www.nature.com/articles/s44385-024-00003-9), *Qian Liao, ..., **Yizheng Wang**, Yijie Ding\*, Quan Zou\*, Ke Han\*. npj Biomedical Innovations*

# 📜 Patents
- *2025.04*: [A Phylogenetic Tree Construction Method Based on Metric Learning](https://cprs.patentstar.com.cn/Search/Detail?ANE=5CBA5BEA9GFE9DHG8GBA4CCA9CGE9DGD9EEC9HAF7FAA9BEF), (No.CN202510533729.3)
- *2024.09*: [A Method for Identifying Nucleic Acid Modification Sites Using Neural Network Models](https://cprs.patentstar.com.cn/Search/Detail?ANE=7BEA9EFA9DHD6BBA6EBA5DCA8CAA9ICEAIBA9GGD9EFG9FGF), (No.CN202410638063.3)
- *2023.11*: [A Construction Method for Biological Sequence Ensemble Classifiers and Methods for Predicting and Classifying Biological Sequences](https://cprs.patentstar.com.cn/Search/Detail?ANE=7EBA8IAA4BBA9GEE9AIA9IGF9HCC9DCAGGIA9AHB9IBD7BAA), (No.CN202310249336.0)
- *2023.03*: [A Training Method and Model for Predicting microRNA-Disease Associations](https://cprs.patentstar.com.cn/Search/Detail?ANE=7DCA9HCA6DBA9CGB9BHA9HBA9HAC9IDG9GFG9GAD8AGA9AGD), (No.CN202211444626.2)

# 🎖 Awards and Funds
- *2024.12*: CSC Scholarship for Study Abroad (公派留学奖学金), China Scholarship Council (国家留学基金管理委员会), *22,800 AUD$*.
- *2022.06*: Outstanding graduates of Hebei Province (河北省优秀毕业生), Hebei Provincial Department of Education (河北省教育厅).

# 📖 Educations
- *2024.09 - (now)*: Ph.D. candidate, [Institute of Fundamental and Frontier Sciences](https://www.iffs.uestc.edu.cn/), [University of Electronic Science and Technology of China](https://www.uestc.edu.cn) (电子科技大学，基础与前沿研究院). &nbsp;<img src='./images/uestc.jpg' style='height: 1.5em;'>&nbsp;
- *2023.07 - (now)*: Ph.D. candidate, [Yangtze Delta Region Institute (Quzhou)](http://ydri.uestc.edu.cn), [University of Electronic Science and Technology of China](https://www.uestc.edu.cn) (电子科技大学，长三角研究院). &nbsp;<img src='./images/ydri.jpg' style='height: 1.5em;'>&nbsp; 
- *2022.09 - 2024.06*: Master, [Institute of Fundamental and Frontier Sciences](https://www.iffs.uestc.edu.cn/), [University of Electronic Science and Technology of China](https://www.uestc.edu.cn) (电子科技大学，基础与前沿研究院). &nbsp;<img src='./images/uestc.jpg' style='height: 1.5em;'>&nbsp;
- *2018.09 - 2022.06*: Bachelor, [School of Information Science and Engineering](http://ise.ysu.edu.cn), [Yanshan University](http://www.ysu.edu.cn) (燕山大学，信息科学与工程学院). &nbsp;<img src='./images/ysu.jpg' style='height: 1.5em;'>&nbsp;
- *2015.09 - 2018.06*: High school student, [Hebei Zhengding Senior High School](http://www.zhengzhong.cn/home.html), [East Campus](http://dongxiaoqu.zhengzhong.cn/) (河北正定中学，东校区). &nbsp;<img src='./images/zz.jpg' style='height: 1.5em;'>&nbsp;

<br>
<div align="center">
Last updated: 2025.06.11
</div>
<br>
